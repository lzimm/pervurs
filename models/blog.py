from pervurs.libs import orm
from pervurs.libs.orm import fields
from pervurs.runtime.store import HotRank

class Blog(orm.Model):
    posts = fields.ModelField(relation=orm.relations['1_to_n'], model='Post')
    user = fields.UserField(relation=orm.relations['n_to_1'], model='User')
    admins = fields.UserField(relation=orm.relations['n_to_n'], model='User')
    host = fields.StringField(len=255)
    
    name = fields.StringField(len=50)
    
    def get_hot_posts(self):
        return self.posts.filter(comments__join=True, group="post.id", order_by="COUNT(comment.id)", limit=6, offset=0).fetchall()
        
    def get_featured_posts(self):
        return self.posts.filter(views__join=True, group="post.id", order_by="COUNT(postview.id)", limit=6, offset=0).fetchall()