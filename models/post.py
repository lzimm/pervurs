import os

from PIL import Image

from pervurs.libs import orm
from pervurs.libs.orm import fields
from pervurs.libs.decorators import deferred_member
from pervurs.deps.s3 import S3
from pervurs.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_ATTACHMENT_BUCKET, DEFAULT_ATTACHMENT_IMAGE, ATTACHMENT_SIZES, WORKING_DIR 

class Post(orm.Model):
    blog = fields.ModelField(relation=orm.relations['n_to_1'], model='Blog')
    user = fields.UserField(relation=orm.relations['n_to_1'], model='User')
    views = fields.ModelField(relation=orm.relations['1_to_n'], model='PostView')
    comments = fields.ModelField(relation=orm.relations['1_to_n'], model='Comment')

    posted = fields.DateField()
    marker = fields.StringField(len=255)
    classes = fields.StringField(len=255)
    title = fields.StringField(len=255)
    span = fields.TextField()
    featured = fields.BooleanField()
    body = fields.TextField()
    style = fields.TextField()
    
    search_id = fields.NumberField()
    
    @deferred_member
    def process_attachment(self, attachment):
        conn = S3.AWSAuthConnection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
        
        attachment = Image.open(attachment)
        for (width, height, crop) in ATTACHMENT_SIZES:
            filename = "%s-%s-%s.png" % (self.id, width, height)
            filepath = os.path.join(WORKING_DIR, filename)
            
            (owidth, oheight) = attachment.size
            
            if crop:
                if (owidth > oheight):
                    fwidth = oheight/height*width
                    fheight = oheight
                    x = (fwidth - owidth)/2
                    y = 0
                else:
                    fwidth = owidth
                    fheight = owidth/width*height
                    x = 0
                    y = (fheight - oheight)/2
            else:
                (fwidth, fheight) = (owidth, oheight)
                (x, y) = (0, 0)
                scale = float(float(width) / float(owidth))
                width = int(owidth*scale)
                height = int(oheight*scale)
            
            dest = Image.new('RGBA', (fwidth, fheight))
            dest.paste(attachment.copy(), (x, y))
            dest = dest.resize((width, height), Image.ANTIALIAS)
            
            dest.save(filepath, 'PNG')
            
            upload = open(filepath)
            conn.put(AWS_ATTACHMENT_BUCKET, filename, upload.read(), {'x-amz-acl': 'public-read' , 'Content-Type': 'image/png'})
            upload.close()
            os.remove(filepath)
        
    def set_default_attachment(self):
        self.process_attachment(open(DEFAULT_ATTACHMENT_IMAGE))