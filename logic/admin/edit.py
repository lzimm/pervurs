from pervurs.libs.decorators import admin
from pervurs.libs.utils import Redirect, NotFound
from pervurs.models import Post

@admin
def http(req):
    req.post = Post.filter(id__is=req.postpath[0], blog__is=req.settings.ref.id).fetchone()
    
    if req.post:
        req.args.setdefault('featured', [req.post.featured])
        req.args.setdefault('marker', [req.post.marker])
        req.args.setdefault('classes', [req.post.classes])
        req.args.setdefault('title', [req.post.title])
        req.args.setdefault('span', [req.post.span])
        req.args.setdefault('body', [req.post.body])
        req.args.setdefault('style', [req.post.style])
        return None
    else:
        return NotFound(req.path)

@admin
def http_POST(req):
    req.post = Post.filter(id__is=req.postpath[0], blog__is=req.settings.ref.id).fetchone()
    
    if req.post:
        req.args.setdefault('featured', [req.post.featured])
        req.args.setdefault('marker', [req.post.marker])
        req.args.setdefault('classes', [req.post.classes])
        req.args.setdefault('title', [req.post.title])
        req.args.setdefault('span', [req.post.span])
        req.args.setdefault('body', [req.post.body])
        req.args.setdefault('style', [req.post.style])
        
        req.post.featured = req.args['featured'][0]
        req.post.marker = req.args['marker'][0]
        req.post.classes = req.args['classes'][0]
        req.post.title = req.args['title'][0]
        req.post.span = req.args['span'][0]
        req.post.body = req.args['body'][0]       
        req.post.style = req.args['style'][0]       
        req.post.save()

        if req.files['attachment'][0][1]:
            req.post.process_attachment(req.files['attachment'][0][2])
        
        return None
    else:
        return NotFound(req.path)