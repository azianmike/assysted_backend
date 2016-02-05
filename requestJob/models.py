from mongoengine import connect, document
from mongoengine.fields import *

connect('assysted_DB')

class job_category(document.Document):
    category_name = StringField(required=True)

class job_request(document.Document):
    '''
    Class for a job request submitted by a user LOOKING for an assystant
    '''
    userId = ObjectIdField(required=True) #user objectID
    email = StringField(required=True)
    stillSearching = BooleanField(required=True, default=True)
    timeOfRequest = DateTimeField()
    description = StringField(required=True)
    userSubmitPrice = IntField(required=True)
    listOfBidders = ListField( field=DictField(), required=True )
    listOfBids = ListField( field=IntField(), required=True )
    jobCategory = StringField(required=True)

class job_search(document.Document):
    '''
    Job search request submitted by a user looking for a JOB
    Submitted by an assystant
    '''
    userId = ObjectIdField(required=True) #user objectID
    email = StringField(required=True)
    stillSearching = BooleanField(required=True, default=True)
    timeOfRequest = DateTimeField()
    userRequestPrice = IntField(required=True)
    jobCategory = StringField(required=True)
