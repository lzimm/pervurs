from datetime import datetime
from pervurs.libs.decorators import admin
from pervurs.models import Post

@admin
def http(req):
    req.args.setdefault('featured', [False])
    req.args.setdefault('marker', ['Connectedism'])
    req.args.setdefault('classes', [''])
    req.args.setdefault('title', [''])
    req.args.setdefault('span', [''])
    req.args.setdefault('body', [''])
    req.args.setdefault('style', [''])
    
    return None

@admin
def http_POST(req):
    req.args.setdefault('featured', [False])
    req.args.setdefault('marker', ['Connectedism'])
    req.args.setdefault('classes', [''])
    req.args.setdefault('title', [''])
    req.args.setdefault('span', [''])
    req.args.setdefault('body', [''])
    req.args.setdefault('style', [''])
    
    post = Post()
    post.blog = req.settings.ref
    post.user = req.user
    post.featured = req.args['featured'][0]
    post.marker = req.args['marker'][0]
    post.classes = req.args['classes'][0]
    post.title = req.args['title'][0]
    post.span = req.args['span'][0]
    post.body = req.args['body'][0]
    post.style = req.args['style'][0]
    post.posted = str(datetime.today())
    post.save()

    if req.files['attachment'][0][1]:
        post.process_attachment(req.files['attachment'][0][2])
    else:
        post.set_default_attachment()

    return None