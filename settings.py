import os.path

SECRET_KEY = ''
QONVO_SITE_ID = ''

AWS_ACCESS_KEY_ID = ""
AWS_SECRET_ACCESS_KEY = ""
AWS_ATTACHMENT_BUCKET = "connectedism.attachments"
AWS_ATTACHMENT_BASE = "http://%s.s3.amazonaws.com" % (AWS_ATTACHMENT_BUCKET)

DEFAULT_ATTACHMENT_IMAGE = "/Life/pervurs/server/www/static/img/default_attachment.png"
ATTACHMENT_SIZES = [(50, 50, True), (100, 100, True), (150, 120, True), (250, 250, False)]
WORKING_DIR = "/Life/pervurs/tmp"

from pervurs.models import Blog

defaultSiteModel = Blog
defaultSiteHost = 'localhost'