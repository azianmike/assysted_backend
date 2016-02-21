from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.

@csrf_exempt
def index(request):

    #Should be an ObjectIdField
    reviewerPost = request.POST.get('reviewer', '')
    #should be an ObjectIdField
    userBeingReviewedPost = request.POST.get('userBeingReviewed', '')
    ratingPost = request.POST.get('rating', '')
    descriptionPost = request.POST.get('description', '')
    return 'hi'