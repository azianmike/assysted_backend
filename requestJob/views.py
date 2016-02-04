from json import dumps

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from requestJob.jobRequestHelper import submitJobRequest


# Create your views here.

@csrf_exempt
def requestJob(request):

    return HttpResponse(dumps(submitJobRequest(request)))
