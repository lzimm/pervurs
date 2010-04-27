from pervurs.libs import orm
from pervurs.libs.orm import fields

class PostView(orm.Model):
    post = fields.ModelField(relation=orm.relations['n_to_1'], model='Post')
    ip = fields.StringField(len=32)