from django.test import TestCase
from requests import post
from json import loads
from reviews.models import Rating
from requestJob.models import job_search
from requestJob.tests import get_user_id, insert_new_user

# Create your tests here.
url = 'http://127.0.0.1:8000/'


class SubmitReviewTest(TestCase):

    def test_submit_review(self):
        #submitting a job search to update the review
        submitPostData = {'userId':get_user_id()}
        submitPostData['email'] = 'testuser@test.com'
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
            checkForJobSearch = job_search.objects.get( userId = get_user_id(), jobCategory='digital design' )
        except job_search.DoesNotExist:
            self.assertEqual(True, False, "Job search does not exist in mongo")

        print 'test_submit_review'
        submitPostData = {'reviewer':insert_new_user('testemail2@test.com', 'blah')}
        submitPostData['userBeingReviewed'] = get_user_id()
        submitPostData['rating'] = 4
        submitPostData['description'] = 'Test review'
        full_url = url+'api/submitReview'
        response = post(full_url, data=submitPostData)
        print full_url
        print str(response.content)
        responseObj = loads(response.content)

        self.assertEqual(responseObj['success'], 1)
        self.assertEqual(responseObj['message'], 'Successfully added review!')

        try:
            checkForRating = Rating.objects.get( reviewer =insert_new_user('testemail2@test.com', 'blah'), userBeingReviewed = get_user_id(), description='Test review' )
            listOfRatings = Rating.objects.filter(userBeingReviewed = get_user_id())
            self.assertEqual(checkForJobSearch.userAvgRating, listOfRatings.aggregate_average("rating"))
            self.assertEqual(checkForJobSearch.userNumRating, listOfRatings.count())
            checkForJobSearch.delete()
            checkForRating.delete()
        except Rating.DoesNotExist:
            self.assertEqual(True, False, "Job search does not exist in mongo")

