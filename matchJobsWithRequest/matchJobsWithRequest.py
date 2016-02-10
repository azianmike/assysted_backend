__author__ = 'michaell'

from requestJob.models import *

while(1):
    #all job requests gotten from DB
    listOfAllJobRequest = job_request.objects.all()
    '''
    Grab all the job_search objects so we dont have to make multiple DB requests
    sort by category
    sort by price?
    sort by rating?
    then match
    then add user to listOfBidders/listOfBids and then send out notification/email
    DO NOT move to old_db until accepted/cancelled

    sorting
    json = job_request.objects.all().to_json()
    json2 = loads(json)
    json2.sort(key=itemgetter('userSubmitPrice')) #sorts in place

    '''
