from json import dumps

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from requestJob.jobRequestHelper import submitJobRequest
from requestJob.jobSubmitHelper import submit_job_search


# Create your views here.

@csrf_exempt
def requestJob(request):

    return HttpResponse(dumps(submitJobRequest(request)))

@csrf_exempt
def submit_job_search(request):

    return HttpResponse(dumps(submit_job_search(request)))