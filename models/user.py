from pervurs.libs import orm
from pervurs.libs.orm import fields
from pervurs.libs.orm.query import Query
from zope.interface import implements

class User(orm.Model):
    implements(orm.IUser)
    
    username = fields.StringField(len=16)
    email = fields.EmailField()
    password = fields.HashedField(len=16)
    posts = fields.ModelField(relation=orm.relations['1_to_n'], model='Post')
    blogs = fields.ModelField(relation=orm.relations['n_to_n'], model='Blog')
    comments = fields.ModelField(relation=orm.relations['1_to_n'], model='Comment')
    
    def __init__(self, row=None):
        orm.Model.__init__(self, row)
        
    def authenticate(self):
        row = Query("""SELECT * FROM user WHERE email = '%s' AND password = '%s' 
                        LIMIT 1""" % (self.email, self.password)).execute().fetchone()
        
        if row:
            return User(row)
        else:
            return None
