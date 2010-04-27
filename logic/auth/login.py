import cPickle
from Crypto.Cipher import ARC4
from datetime import datetime
from pervurs.libs.qonvo.auth import login
from pervurs.libs.utils import Redirect
from pervurs.settings import SECRET_KEY
from StringIO import StringIO
from twisted.web2.http_headers import Cookie
from urllib import unquote_plus

def http(req):
    return None

def http_POST(req):
    user = login(req.args['email'][0], req.args['password'][0])

    if user:
        user['ip'] = req.remoteAddr.host

        dump = StringIO()
        cPickle.dump(user, dump)
        userdata = dump.getvalue()
        dump.close()

        userdata = ''.join(ARC4.new(SECRET_KEY).encrypt(userdata).encode('base64').splitlines()).strip()

        req.cookies.append(Cookie('auth',userdata,path='/'))
        req.cookies.append(Cookie('qonvo_auth',user['hash'],path='/'))
        req.cookies.append(Cookie('qonvo_user_id',user['id'],path='/'))
        req.cookies.append(Cookie('qonvo_dirty',str(datetime.today()),path='/'))
        
        if req.args.get('p', None):
            return Redirect(unquote_plus(req.args['p'][0]))
        else:
            return Redirect('/')
    
    return None