import simplejson as json

from pervurs.models import Post, User, Comment
from pervurs.runtime.store import HotRank

def http(req):
    return None

def http_POST(req):
    message = json.loads(req.args['message'][0])
    for data in data.posts:    
        post = Post.get(data.ident)
        user = User.get(data.user)

        if not user:
            user = User()
            user.id = data.user
            user.username = data.name
            user.email = data.email
            user.save()            

        if post:
            comment = Comment()
            comment.post = post
            comment.user = user
            comment.id = data.id
            comment.posted = data.time
            comment.title = data.title
            comment.body = data.body
            comment.save()       
    
    return None