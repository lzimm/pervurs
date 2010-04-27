from pervurs.libs.utils import Redirect, NotFound

def http(req):
    if len(req.postpath) > 2 and req.postpath[2]:
        post_filter = req.settings.ref.posts.filter(posted__date='-'.join(req.postpath[0:3]), limit=req.args.get('limit', [10])[0], offset=req.args.get('page', [0])[0])
    elif len(req.postpath) > 1 and req.postpath[1]:
        post_filter = req.settings.ref.posts.filter(posted__month=''.join(req.postpath[0:2]), limit=req.args.get('limit', [10])[0], offset=req.args.get('page', [0])[0])
    elif len(req.postpath) > 0 and req.postpath[0]:
        post_filter = req.settings.ref.posts.filter(posted__year=req.postpath[0], limit=req.args.get('limit', [10])[0], offset=req.args.get('page', [0])[0])
    else:
        return Redirect('/')
        
    req.posts = post_filter.fetchall(count=True)
    req.pagination = post_filter
    
    return None