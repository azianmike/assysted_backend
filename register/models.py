from mongoengine import connect, document
from mongoengine.fields import *

connect('assysted_DB')

class User(document.Document):
    email = StringField(required=True)
    password = StringField(required=True)
    activated = BooleanField(required=True)
    joinDate = DateTimeField()
    avgRating = DecimalField(precision=3,required=True, default=0)
    numRatings = IntField(required=True, default=0)
