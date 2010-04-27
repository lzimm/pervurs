import sys, traceback
sys.path.append("/Life")

import os.path, time
import pervurs.server
from twisted.web2 import server, http, resource, channel, iweb, stream, static
from twisted.internet import defer
from Cheetah.Template import Template
from pervurs import import_mod, settings
from pervurs.server.www import import_tmpl
from pervurs.libs.utils import HardResponder
from pervurs.server.www.bindings import middleware_bindings

from pervurs.libs.orm.query import Query

logic_tree = dict()
view_tree = dict()
site_tree = {settings.defaultSiteHost:
                settings.defaultSiteModel.filter(host__is = settings.defaultSiteHost).fetchone()}

class PervursHTTP(resource.Resource):
    addSlash = True
    siteResource = settings.defaultSiteModel
    defaultHost = settings.defaultSiteHost
    
    def __init__(self, logic_mod, path, mode = 'http'):
        self.logic_mod = logic_mod
        self.path = path
        self.mode = mode
        
        if '__val__' not in view_tree:
            logic_tree['__val__'] = import_mod('.'.join([self.logic_mod,'index']))
            view_tree['__val__'] = import_tmpl('index')

    def locateChild(self, req, segs):
        if site_tree.get(req.host, None) is None:
            site_tree[req.host] = self.siteResource.filter(host__is = req.host).fetchone()
        
        settings = SiteSettings(site_tree[req.host], site_tree[self.defaultHost])
        
        req.settings = settings
        
        for binding in middleware_bindings:
            binding(req)
        
        try:
            [self.mode, name] = segs[0].split('-')
        except:
            name = segs[0]
        
        if name == '' and len(segs) == 1:
            return self, server.StopTraversal
        if os.path.isfile(os.path.join(self.path, name)):
            return PervursHTTPStatic(self, os.path.join(self.path, name)), server.StopTraversal
        elif os.path.exists(os.path.join(self.path, name)):
            return PervursHTTPStatic(self, os.path.join(self.path, name)), segs[1:]
        else:
            logicpath = '.'.join([self.logic_mod,name])

            if name not in view_tree:
                try:
                    try:
                        logic_tree[name] = {'__val__':import_mod(logicpath)}
                    except:
                        pass

                    view_tree[name] = {'__val__':import_tmpl(name)}
                except:
                    return self, server.StopTraversal

            return PervursHTTPView(self, name, view_tree[name], logicpath, logic_tree[name], self.mode), segs[1:]

    def renderHTTP(self, req):            
        responder = getattr(logic_tree['__val__'], self.mode, logic_tree['__val__'].http)(req)
        view = view_tree['__val__']()
        view.req = req
        
        response = http.Response(200, stream=stream.MemoryStream(view.respond().encode('utf8')))
        response.headers.setRawHeaders('Content-Type', ['text/html; charset=utf-8'])
        
        if responder:
            responder(response)
        return response      

class PervursHTTPView(resource.Resource):
    addSlash = True

    def __init__(self, root, viewpath, view, logicpath, logic, mode = 'http'):
        self.root = root
        self.viewpath = viewpath
        self.logicpath = logicpath
        self.view = view
        self.logic = logic
        self.mode = mode
        
    def locateChild(self, req, segs):
        name = segs[0]
        
        self.logicpath = '.'.join([self.logicpath,name])
        self.viewpath = '.'.join([self.viewpath,name])
        
        if name == '' and len(segs) == 1:
            return self, server.StopTraversal
        elif name not in self.view:
            try:
                self.view[name] = {'__val__':import_tmpl(self.viewpath)}
                self.view = self.view[name]
                
                try:
                    if type(self.logic) is not type([]):
                        self.logic[name] = {'__val__':import_mod(self.logicpath)}
                        self.logic = self.logic[name]
                except:
                    self.logic = [self.logic]
            except:
                return self, server.StopTraversal
        else:
            self.view = self.view[name]
            try:
                if type(self.logic) is not type([]):
                    self.logic = self.logic[name]
            except:
                self.logic = self.logic
        return self, segs[1:]

    def renderHTTP(self, req):
        if type(self.logic) is type([]):
            self.logic = self.logic[0]
        
        mode = self.mode + '_' + req.method
        logic = getattr(self.logic['__val__'], mode, self.logic['__val__'].http)
        
        if req.method == 'POST':
            return server.parsePOSTData(req).addCallback(self.__render, *[req, logic])
        else:
            response = self.__render(None, req, logic)
            return defer.succeed(response)
    
    def __render(self, dcb, req, logic):
        responder = logic(req)
        
        if isinstance(responder, HardResponder):
            return responder.response(getattr(req, 'cookies', None))
            
        view = self.view['__val__']()
        view.req = req
        response = http.Response(200, stream=stream.MemoryStream(view.respond().encode('utf8')))
        response.headers.setRawHeaders('Content-Type', ['text/html; charset=utf-8'])
        
        if getattr(req, 'cookies', None):
            response.headers.setHeader('Set-Cookie',req.cookies)

        if responder:
            responder(response)
        return response
    
class PervursHTTPStatic(resource.Resource):
    addSlash = True

    def __init__(self, root, path):
        self.root = root
        self.path = path

    def locateChild(self, req, segs):
        name = segs[0]
        self.path = os.path.join(self.path, name)
        if not os.path.exists(self.path):
            return None, server.StopTraversal
        elif os.path.isdir(self.path):
            return PervursHTTPStatic(self.root, self.path), segs[1:]
        else:
            return self, server.StopTraversal

    def renderHTTP(self, req):
        if os.path.isfile(self.path):
            return static.File(self.path)
        else:
            return http.Response(200, stream=stream.MemoryStream('forbidden'))

site = server.Site(PervursHTTP('pervurs.logic',
                    os.path.join(os.path.dirname(os.getcwd()), 'server/www/static')))

class SiteSettings(object):
    def __init__(self, ref, alt):
        if ref is None:
            ref = alt
        
        self.ref = ref
        self.hostpaths = {
                'stylesheet': "/custom/css/%s.css" % ref.id
            }

from twisted.application import service, strports
application = service.Application("pervurs")
service = strports.service('tcp:80', channel.HTTPFactory(site))
service.setServiceParent(application)