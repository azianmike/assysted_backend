from mongoengine import connect
from mongoengine.fields import *

connect('assysted_DB')

class User(Document):
    email = StringField(required=True)
    password = StringField(required=True)
    activated = BooleanField(required=True)
    joinDate = DateTimeField()
