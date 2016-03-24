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
    #Instant match: matches with a search if the userAvgRating >=4.5 and userNumRating >=5
    instantMatch = BooleanField(required=True, default=False)
    completed = BooleanField(required=True, default=False)

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
    userAvgRating = DecimalField(precision=3,required=True, default=0)
    userNumRating = IntField(required=True, default=0)


class old_job_request(document.Document):
    '''
    Class for a job request that has either been filled or cancelled or expired
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

class old_job_search(document.Document):
    '''
    Job search request submitted by a user looking for a JOB
    that has been cancelled/filled
    Submitted by an assystant

    '''
    userId = ObjectIdField(required=True) #user objectID
    email = StringField(required=True)
    stillSearching = BooleanField(required=True, default=True)
    timeOfRequest = DateTimeField()
    userRequestPrice = IntField(required=True)
    jobCategory = StringField(required=True)