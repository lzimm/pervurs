from pervurs.libs import orm
from pervurs.libs.orm import fields

class SearchSuggestion(orm.Model):
    suggestion = fields.StringField(len=255)
    frequency = fields.NumberField()