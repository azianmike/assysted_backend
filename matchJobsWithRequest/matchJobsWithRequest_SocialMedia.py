from operator import itemgetter

__author__ = 'michaell'
from requestJob.models import *
from json import loads

while(1):
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

    need to figure out how many job requests can one job search be matched with
    possible solutions: only one request is matched with a search, instant match?
    possible solution: a search is allowed to match with top 3 requests
    possible solution: a request has a field that is instant match or not instant match, if not, then only 3 requests can be matched

    #####BEST SOLUTION#####
    make everything "instant match" for now (on demand economy)
    make sure to tell user we WON'T charge them until we have vetted their stuff
    match requests with highest rated searches
    for now, set $10/hr constant and only have reviews as defining factor
    user sets how long they think it will take
    matches with search, asks assystant how long they think it will take
    for now, if <=request set time, then we match (i.e. requestor says will take 5 hrs, assystant says will take 6 hrs, dont match)
    if more than 2 assystants say it will take longer than said, then we tell the requestor to increase time


    is it better to continuously poll and try to match?
    or match with every request sent?

    sorting
    json = job_request.objects.all().to_json()
    json2 = loads(json)
    json2.sort(key=itemgetter('userSubmitPrice')) #sorts in place

    '''
    #list of all job REQUESTS
    listOfAllJobRequest = job_request.objects.filter(jobCategory='social media')[:50]
    listOfAllJobRequest = loads(listOfAllJobRequest.to_json())
    #list of all job SEARCHES
    listOfAllJobSearches = job_search.objects.filter(jobCategory='social media')[:50]
    listOfAllJobSearches = loads(listOfAllJobSearches.to_json())
    listOfAllJobSearches.sort(key=itemgetter('userAvgRating', 'userNumRating', 'userSubmitPrice')) #sorts in place


