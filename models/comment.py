from pervurs.libs import orm
from pervurs.libs.orm import fields

class Comment(orm.Model):
    post = fields.ModelField(relation=orm.relations['n_to_1'], model='Post')
    user = fields.UserField(relation=orm.relations['n_to_1'], model='User')
    
    posted = fields.DateField()
    title = fields.StringField(len=255)
    body = fields.TextField()