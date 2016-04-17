from django.test import TestCase
from requests import post
from json import loads
from requestJob.models import job_search, job_request
from register.views import register_user_helper
from login.loginHelper import loginWithEmailAndPassword

# Create your tests here.
url = 'http://127.0.0.1:8000/'


def get_user_id():
    response = register_user_helper('testuser@test.com', 'testpassword')
    if response['success'] == -1:
        loginResponse = loginWithEmailAndPassword('testuser@test.com', 'testpassword')
        return loginResponse['id']
    return response['id']

def insert_new_user(email, password):
    response = register_user_helper(email, password)
    if response['success'] == -1:
        loginResponse = loginWithEmailAndPassword(email, password)
        return loginResponse['id']
    return response['id']


class JobSearchTests(TestCase):

    def test_submit_search(self):
        print 'test_submit_search'

        submitPostData = {'userId':get_user_id()}
        submitPostData['email'] = 'testuser@test.com'
        submitPostData['userSearchPrice'] = 10
        submitPostData['jobCategory'] = 'digital design'
        full_url = url+'api/searchJob'
        response = post(full_url, data=submitPostData)
        print full_url
        print 'response'
        print str(response.content)
        responseObj = loads(response.content)

        self.assertEqual(responseObj['success'], 1)
        self.assertEqual(responseObj['message'], 'Job request successful')

        try:
            checkForJobSearch = job_search.objects.get( userId = get_user_id(), userRequestPrice = 10, jobCategory='digital design' )
            checkForJobSearch.delete()
        except job_search.DoesNotExist:
            self.assertEqual(True, False, "Job search does not exist in mongo")

    def test_submit_request(self):
        print 'test_submit_request'
        response = register_user_helper('testuser@test.com', 'testpassword')

        submitPostData = {'userId':get_user_id()}
        submitPostData['email'] = 'testuser@test.com'
        submitPostData['jobCategory'] = 'digital design'
        submitPostData['description'] = 'TESTING A DESCRIPTION'

        full_url = url+'api/requestJob'
        response = post(full_url, data=submitPostData)
        print full_url
        print 'response'
        print str(response.content)
        responseObj = loads(response.content)

        self.assertEqual(responseObj['success'], 1)
        self.assertEqual(responseObj['message'], 'Job request successful')

        try:
            checkForJobSearch = job_request.objects.get( userId = get_user_id(), userSubmitPrice = 50, jobCategory='digital design' )
            checkForJobSearch.delete()
        except job_search.DoesNotExist:
            self.assertEqual(True, False, "Job request does not exist in mongo")

    def test_submit_request_invalid_price(self):
        print 'test_submit_request_invalid_price'
        response = register_user_helper('testuser@test.com', 'testpassword')

        submitPostData = {'userId':get_user_id()}
        submitPostData['email'] = 'testuser@test.com'
        submitPostData['userRequestPrice'] = 1
        submitPostData['jobCategory'] = 'digital design'
        submitPostData['description'] = 'TESTING A DESCRIPTION'

        full_url = url+'api/requestJob'
        response = post(full_url, data=submitPostData)
        print full_url
        print 'response'
        print str(response.content)
        responseObj = loads(response.content)

        self.assertEqual(responseObj['success'], -1)
        self.assertEqual(responseObj['message'], 'Invalid request price')
