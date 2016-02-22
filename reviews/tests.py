from django.test import TestCase
from requests import post
from json import loads
from reviews.models import Rating

# Create your tests here.
url = 'http://ec2-52-71-164-78.compute-1.amazonaws.com/'
class SubmitReviewTest(TestCase):

    def test_submit_review(self):
        print 'test_submit_review'
        submitPostData = {'reviewer':'56b2cd3e3907c32099dbad18'}
        submitPostData['userBeingReviewed'] = '56aeec653907c30d1b276594'
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
            checkForJobSearch = Rating.objects.get( reviewer = '56b2cd3e3907c32099dbad18', userBeingReviewed = '56aeec653907c30d1b276594', description='Test review' )
            checkForJobSearch.delete()
        except Rating.DoesNotExist:
            self.assertEqual(True, False, "Job search does not exist in mongo")

