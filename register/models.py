from mongoengine import connect, document
from mongoengine.fields import *

connect('assysted_DB')

class User(document.Document):
    email = StringField(required=True)
    password = StringField(required=True)
    activated = BooleanField(required=True)
    joinDate = DateTimeField()
