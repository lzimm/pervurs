from pervurs.models import Post, PostView
from pervurs.libs.utils import Redirect, NotFound

def http(req):
    if len(req.postpath) > 3 and req.postpath[3]:
        req.post = Post.filter(posted__date='-'.join(req.postpath[0:3]), title__is=req.postpath[3].replace('_', ' ')).fetchone()
        
        if req.post:
            view = PostView()
            view.post = req.post
            view.ip = req.remoteAddr.host
            view.save()
            return None
        else:
            return NotFound(req.path)
    else:
        return Redirect('/archive/' + '/'.join(req.postpath))