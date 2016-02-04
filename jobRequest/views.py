from django.http import HttpResponse
from json import dumps
from django.views.decorators.csrf import csrf_exempt
from jobRequest.jobRequestHelper import submitJobRequest

# Create your views here.

@csrf_exempt
def requestJob(request):

    return HttpResponse(dumps(submitJobRequest(request)))
