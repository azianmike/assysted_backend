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
    email = StringField(required=True) #user email who submitted this job request
    stillSearching = BooleanField(required=True, default=True) #still searching for someone to complete job
    timeOfRequest = DateTimeField()
    #user description of what they want to be completed in the job
    description = StringField(required=True)
    #we default price to 50 for now, this is PER HOUR
    userSubmitPrice = IntField(default=50)
    #job category that the request is in, for now we're just doing digital design
    jobCategory = StringField(required=True, default='digital design')
    #if the job has been completed
    completed = BooleanField(required=True, default=False)
    #number of hours that the requestor thinks it will take (tell to overestimate)
    numberOfHours = IntField( required=True, default=5 )

class job_search(document.Document):
    '''
    Job search request submitted by a user looking for a JOB
    Submitted by an assystant
    '''
    userId = ObjectIdField(required=True) #user objectID
    #email of the person who's SEARCHING for a job
    email = StringField(required=True)
    #if the person is still searching for a job
    stillSearching = BooleanField(required=True, default=True)
    timeOfRequest = DateTimeField()
    #the price that the user is charging, we do not need this for now (as everything is defaulted to flat fee of $50)
    userRequestPrice = IntField(required=False)
    #the job category that the user wants to do a job in, for now default to "digital design"
    jobCategory = StringField(required=True, default='digital design')
    #the avg rating of the user looking for a job
    userAvgRating = DecimalField(precision=3,required=True, default=0)
    #the number of ratings of the user looking for a job
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