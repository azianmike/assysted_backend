from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from re import match
from django.template.defaulttags import csrf_token
from json import dumps
import datetime
from hashlib import sha224
from .models import User


def checkValidEmail(email):
    pattern = r"(^[^@]+@[^@]+\.[^@]+)"
    return bool(match(pattern,email))

@csrf_exempt
def index(request):
    emailPost = request.POST.get("email", "")
    passwordPost = request.POST.get("password", "")
    returnDict = {}

    try:
        checkOld = User.objects.get(email=emailPost)
        returnDict['success']=-1
        returnDict['message']="Email is already registered!"
        return HttpResponse(dumps(returnDict))
    except User.DoesNotExist:
        if not checkValidEmail(emailPost):
            returnDict['success'] = -1
            returnDict['message']='Invalid email address'
            return HttpResponse(dumps(returnDict))
        #f='%Y-%m-%d'
        #now = datetime.datetime.now()
        #mysqlTime = now.strftime(f)
        #userToAdd = User.objects.create(_id=emailPost, password=passwordPost, joinDate=mysqlTime)
        import datetime
        joinDateTime = datetime.datetime.now()
        userToAdd = User(email=emailPost, password=passwordPost, activated=True, joinDate = joinDateTime)
        userToAdd.save()
        returnDict['success']= 1
        returnDict['message'] = "Registered! Check your email to activate your account"
        return HttpResponse(dumps(returnDict))                

