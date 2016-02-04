from mongoengine import connect, document
from mongoengine.fields import *

connect('assysted_DB')

class JobRequest(document.Document):
    email = StringField(required=True)
    stillSearching = BooleanField(required=True)
    timeOfRequest = DateTimeField()
    description = StringField(required=True)
    userSubmitPrice = IntField(required=True)
    listOfBidders = ListField( field=[ObjectIdField, StringField ], required=True )
    listOfBids = ListField( field=IntField, required=True )

