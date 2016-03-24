from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from login.loginHelper import check_user_id_exists
from reviews.models import Rating
from requestJob.helper_func import create_return_dict
from json import dumps
from register.models import User
from requestJob.models import job_search

# Create your views here.

@csrf_exempt
def index(request):

    #Should be an ObjectIdField
    reviewerPost = request.POST.get('reviewer', '')
    #should be an ObjectIdField
    userBeingReviewedPost = request.POST.get('userBeingReviewed', '')
    ratingPost = request.POST.get('rating', '')
    descriptionPost = request.POST.get('description', '')

    return HttpResponse(dumps(put_review_in(reviewerPost, userBeingReviewedPost, ratingPost, descriptionPost)))


def put_review_in(reviewerPost, userBeingReviewedPost, ratingPost, descriptionPost):
    '''
    Puts review into database if User IDs for reviewer and person being reviewed exist
    :param reviewerPost:
    :param userBeingReviewedPost:
    :param ratingPost:
    :param descriptionPost:
    :return:
    '''
    if check_user_id_exists(reviewerPost) and check_user_id_exists(userBeingReviewedPost):
        listOfNewAvgAndCount = update_user_rating(userBeingReviewedPost)
        update_job_search_rating(userBeingReviewedPost, listOfNewAvgAndCount)
        ratingToAdd = Rating(reviewer=reviewerPost, userBeingReviewed=userBeingReviewedPost, rating=int(ratingPost), description=descriptionPost)
        ratingToAdd.save()
        return create_return_dict(1, 'Successfully added review!')

    return create_return_dict(-1, 'Users do not exist')

def update_user_rating(userBeingReviewedInput):
    '''
    Updates the user being reviewed's average rating
    :param userBeingReviewed: user to update
    :return: a list with the user avg rating as first indx and num rating as second indx
    '''
    setOfUserRatings = Rating.objects.filter(userBeingReviewed=userBeingReviewedInput)
    newAvg = setOfUserRatings.aggregate_average("rating")
    userToEdit = User.objects.get(id=userBeingReviewedInput)
    userToEdit.avgRating = newAvg
    userToEdit.numRatings = setOfUserRatings.count()
    userToEdit.save()

    return [newAvg, setOfUserRatings.count()]

def update_job_search_rating(userBeingReviewed, listOfNewAvgAndCount ):
    '''
    If the user has any job searches, we must also update the userAvgRating and
    userNumRating fields in the job searches so it's always up to date
    :param userBeingReviewed:
    :param listOfNewAvgAndCount: the first indx is userAvg and second is count of ratings
    :return:
    '''
    setOfJobSearches = job_search.objects.filter( userId=userBeingReviewed )
    setOfJobSearches.userAvgRating = listOfNewAvgAndCount[0]
    setOfJobSearches.userNumRating = listOfNewAvgAndCount[1]
    setOfJobSearches.save()