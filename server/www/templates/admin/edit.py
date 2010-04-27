#!/usr/bin/env python




##################################################
## DEPENDENCIES
import sys
import os
import os.path
from os.path import getmtime, exists
import time
import types
import __builtin__
from Cheetah.Version import MinCompatibleVersion as RequiredCheetahVersion
from Cheetah.Version import MinCompatibleVersionTuple as RequiredCheetahVersionTuple
from Cheetah.Template import Template
from Cheetah.DummyTransaction import DummyTransaction
from Cheetah.NameMapper import NotFound, valueForName, valueFromSearchList, valueFromFrameOrSearchList
from Cheetah.CacheRegion import CacheRegion
import Cheetah.Filters as Filters
import Cheetah.ErrorCatchers as ErrorCatchers
from pervurs.server.www.templates.admin.base import base
from pervurs.includes.urls import links

##################################################
## MODULE CONSTANTS
try:
    True, False
except NameError:
    True, False = (1==1), (1==0)
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '2.0.1'
__CHEETAH_versionTuple__ = (2, 0, 1, 'final', 0)
__CHEETAH_genTime__ = 1244608040.4196141
__CHEETAH_genTimestamp__ = 'Tue Jun  9 21:27:20 2009'
__CHEETAH_src__ = 'admin/edit.tmpl'
__CHEETAH_srcLastModified__ = 'Sun Apr 19 11:13:35 2009'
__CHEETAH_docstring__ = 'Autogenerated by CHEETAH: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class edit(base):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        base.__init__(self, *args, **KWs)
        if not self._CHEETAH__instanceInitialized:
            cheetahKWArgs = {}
            allowedKWs = 'searchList namespaces filter filtersLib errorCatcher'.split()
            for k,v in KWs.items():
                if k in allowedKWs: cheetahKWArgs[k] = v
            self._initCheetahInstance(**cheetahKWArgs)
        

    def scripts(self, **KWS):



        ## CHEETAH: generated from #block scripts at line 4, col 1.
        trans = KWS.get("trans")
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write('''
<script type="text/javascript" src="/fckeditor/fckeditor.js"></script>
<script type="text/javascript">
window.onload = function()
{
var oFCKeditor = new FCKeditor( \'body\' ) ;
oFCKeditor.BasePath = "/fckeditor/";
oFCKeditor.ReplaceTextarea();
}
</script>

''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def body(self, **KWS):



        ## CHEETAH: generated from #block body at line 18, col 1.
        trans = KWS.get("trans")
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write('''
<div id="blog_editor">
    <form action="''')
        _v = VFFSL(SL,"req.uri",True) # '$req.uri' on line 21, col 19
        if _v is not None: write(_filter(_v, rawExpr='$req.uri')) # from line 21, col 19.
        write('''" method="POST" enctype="multipart/form-data">
\t<div class="blog_post">
\t\t<div class="blog_marker"><input type="text" name="marker" value="''')
        _v = VFN(VFFSL(SL,"req.args",True),"marker",True)[0] # '$req.args.marker[0]' on line 23, col 68
        if _v is not None: write(_filter(_v, rawExpr='$req.args.marker[0]')) # from line 23, col 68.
        write('''" /></div>
\t\t<div class="blog_classes"><input type="text" name="classes" value="''')
        _v = VFN(VFFSL(SL,"req.args",True),"classes",True)[0] # '$req.args.classes[0]' on line 24, col 70
        if _v is not None: write(_filter(_v, rawExpr='$req.args.classes[0]')) # from line 24, col 70.
        write('''" /></div>
\t\t<div class="blog_title"><input type="text" name="title" value="''')
        _v = VFN(VFFSL(SL,"req.args",True),"title",True)[0] # '$req.args.title[0]' on line 25, col 66
        if _v is not None: write(_filter(_v, rawExpr='$req.args.title[0]')) # from line 25, col 66.
        write('''" /></div>
\t\t<div class="blog_span"><textarea name="span">''')
        _v = VFN(VFFSL(SL,"req.args",True),"span",True)[0] # '$req.args.span[0]' on line 26, col 48
        if _v is not None: write(_filter(_v, rawExpr='$req.args.span[0]')) # from line 26, col 48.
        write('''</textarea></div>
\t\t<div class="blog_body"><textarea name="body">''')
        _v = VFN(VFFSL(SL,"req.args",True),"body",True)[0] # '$req.args.body[0]' on line 27, col 48
        if _v is not None: write(_filter(_v, rawExpr='$req.args.body[0]')) # from line 27, col 48.
        write('''</textarea></div>
\t\t<div class="blog_style"><textarea name="style">''')
        _v = VFN(VFFSL(SL,"req.args",True),"style",True)[0] # '$req.args.style[0]' on line 28, col 50
        if _v is not None: write(_filter(_v, rawExpr='$req.args.style[0]')) # from line 28, col 50.
        write('''</textarea></div>
\t\t<div class="blog_attachment"><input type="file" name="attachment"></div>
\t</div>
\t
\t<div class="blog_options"><input type="submit" /></div>
    </form>
</div>

''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def writeBody(self, **KWS):



        ## CHEETAH: main method generated for this template
        trans = KWS.get("trans")
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write('''
''')
        self.scripts(trans=trans)
        write('''
''')
        self.body(trans=trans)
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        
    ##################################################
    ## CHEETAH GENERATED ATTRIBUTES


    _CHEETAH__instanceInitialized = False

    _CHEETAH_version = __CHEETAH_version__

    _CHEETAH_versionTuple = __CHEETAH_versionTuple__

    _CHEETAH_genTime = __CHEETAH_genTime__

    _CHEETAH_genTimestamp = __CHEETAH_genTimestamp__

    _CHEETAH_src = __CHEETAH_src__

    _CHEETAH_srcLastModified = __CHEETAH_srcLastModified__

    _mainCheetahMethod_for_edit= 'writeBody'

## END CLASS DEFINITION

if not hasattr(edit, '_initCheetahAttributes'):
    templateAPIClass = getattr(edit, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(edit)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=edit()).run()

