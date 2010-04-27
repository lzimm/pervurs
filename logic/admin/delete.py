from pervurs.libs.decorators import admin
from pervurs.models import Post

@admin
def http(req):
    req.post = Post.filter(id__is=req.postpath[0], blog__is=req.settings.ref.id).fetchone()
    
    if req.post:
        return None
    else:
        return NotFound(req.path)