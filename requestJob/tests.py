from django.test import TestCase
from requests import post
from json import loads
from requestJob.models import job_search

# Create your tests here.
url = 'http://ec2-52-71-164-78.compute-1.amazonaws.com/'
class JobSearchTests(TestCase):

    def test_submit_search(self):
        submitPostData = {'userId':'56b2cd3e3907c32099dbad18'}
        submitPostData['email'] = 'testhash2@test.com'
        submitPostData['userRequestPrice'] = 10
        submitPostData['jobCategory'] = 'copywriting'
        full_url = url+'api/searchJob'
        response = post(full_url, data=submitPostData)
        print full_url
        print 'response\n'
        print str(response.content)
        responseObj = loads(response.content)

        self.assertEqual(responseObj['success'], 1)
        self.assertEqual(responseObj['message'], 'Job request successful')

        try:
            checkForJobSearch = job_search.objects.get( userId = '56b2cd3e3907c32099dbad18', userRequestPrice = 10, jobCategory='TestingCategory' )
            checkForJobSearch.delete()
        except job_search.DoesNotExist:
            self.assertEqual(True, False, "Job search does not exist in mongo")

    def test_submit_request(self):
        submitPostData = {'userId':'56b2cd3e3907c32099dbad18'}
        submitPostData['email'] = 'testhash2@test.com'
        submitPostData['userRequestPrice'] = 10
        submitPostData['jobCategory'] = 'copywriting'
        submitPostData['description'] = 'TESTING A DESCRIPTION'

        full_url = url+'api/requestJob'
        response = post(full_url, data=submitPostData)
        print full_url
        print 'response\n'
        print str(response.content)
        responseObj = loads(response.content)

        self.assertEqual(responseObj['success'], 1)
        self.assertEqual(responseObj['message'], 'Job request successful')

        try:
            checkForJobSearch = job_search.objects.get( userId = '56b2cd3e3907c32099dbad18', userRequestPrice = 10, jobCategory='TestingCategory' )
            checkForJobSearch.delete()
        except job_search.DoesNotExist:
            self.assertEqual(True, False, "Job search does not exist in mongo")
