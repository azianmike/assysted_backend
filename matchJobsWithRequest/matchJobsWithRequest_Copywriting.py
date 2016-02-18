__author__ = 'michaell'

from requestJob.models import *
from json import loads

while(1):
    #all job requests gotten from DB
    #only get
    listOfAllJobRequest = job_request.objects.filter(jobCategory='copywriting')[:50]
    listOfAllJobRequest = loads(listOfAllJobRequest.to_json())
    '''
    Grab all the job_search objects so we dont have to make multiple DB requests
    sort by category
    sort by price? rewrite so everything is $10/hr for now. $12?
    make $10 bid minimum. Then match with list of bidders up to 5, with varying amounts of reviews
    have an "instant" accept field to instantly accept any bid from a "good" reviewed job searcher
    sort by rating?
    then match
    then add user to listOfBidders/listOfBids and then send out notification/email
    DO NOT move to old_db until accepted/cancelled

    sorting
    json = job_request.objects.all().to_json()
    json2 = loads(json)
    json2.sort(key=itemgetter('userSubmitPrice')) #sorts in place

    '''
    listOfAllJobSearches = job_search.objects.filter(jobCategory='copywriting')[:50]
    listOfAllJobSearches = loads(listOfAllJobSearches.to_json())


