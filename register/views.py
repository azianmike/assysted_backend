from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from re import match
from json import dumps
import datetime
from .models import User
from hashPasswords import passwords

def checkValidEmail(email):
    pattern = r"(^[^@]+@[^@]+\.[^@]+)"
    return bool(match(pattern,email))

@csrf_exempt
def index(request):
    emailPost = request.POST.get("email", "")
    passwordPost = request.POST.get("password", "")

    return register_user(emailPost, passwordPost)


def register_user(emailPost, passwordPost):
    '''
    Registers the user
    :param emailPost: email passed in from post
    :param passwordPost: password passed in from post
    :return: an HTTP resposne with a error code (if one) and a message of the error
    '''

    return HttpResponse(dumps(register_user_helper(emailPost, passwordPost)))

def register_user_helper(emailPost, passwordPost):
    returnDict = {}

    try:
        checkOld = User.objects.get(email=emailPost)
        returnDict['success'] = -1
        returnDict['message'] = "Email is already registered!"
        return returnDict
    except User.DoesNotExist:
        if not checkValidEmail(emailPost):
            returnDict['success'] = -1
            returnDict['message'] = 'Invalid email address'
            return returnDict

        from datetime import datetime
        joinDateTime = datetime.now()
        hashedPassword = passwords.hashPassword(passwordPost, emailPost)
        userToAdd = User(email=emailPost, password=hashedPassword, activated=True, joinDate=joinDateTime)
        userToAdd.save()
        returnDict['success'] = 1
        returnDict['message'] = "Registered! Check your email to activate your account"
        returnDict['id'] = str(userToAdd.id)
        return returnDict

