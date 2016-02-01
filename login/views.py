from json import dumps

from django.views.decorators.csrf import csrf_exempt
from login.loginHelper import loginUser, checkObjectID
from django.http import HttpResponse


# Create your views here.

@csrf_exempt
def index(request):

    return HttpResponse(dumps(loginUser(request)))

    # return HttpResponse(dumps(returnDict))


@csrf_exempt
def testObjectIdExists(request):
    return HttpResponse(dumps(checkObjectID(request)))
