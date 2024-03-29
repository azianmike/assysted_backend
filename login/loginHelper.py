from json import dumps
from register.models import User
from hashPasswords import passwords

__author__ = 'michaell'


def loginUser(request):
    '''
    Logs in a user if exists and return JSON object to return back to user.
    Note that if successfully logged in, return object will have an objectID for the user
    :param request: HTTP Request params/body/etc
    :return: return a JSON object with status on fail/success, if success, will have objectID for logged in user
    '''

    # get post PARAMS
    emailPost = request.POST.get("email", "")
    passwordPost = request.POST.get("password", "")

    #try catch to see if user exists
    return loginWithEmailAndPassword(emailPost, passwordPost)


def loginWithEmailAndPassword(emailPost, passwordPost):
    '''
    Logs a user in with an email and a password
    :param emailPost: email to log in with (if valid)
    :param passwordPost: password to log in with (if valid)
    :return: returns a dict with a 'success' message and a success code
    '''
    returnDict = {}
    returnDict['success'] = -1

    try:
        hashedPassword = passwords.hashPassword(passwordPost, emailPost)
        checkForUser = User.objects.get(email=emailPost, password=hashedPassword)
        if checkForUser.activated == False:
            returnDict['success'] = -3
            returnDict['message'] = 'Please activate your email'
            return returnDict
        returnDict['success'] = 1
        returnDict['id'] = str(checkForUser.id)
        return returnDict
    except User.DoesNotExist:
        returnDict['success'] = 0
        returnDict['message'] = 'Email does not exist or password is not correct'
        return returnDict


def checkUserID(request):
    '''
    Checks if the user ID is a valid user id
    :param request:
    :return:
    '''
    returnDict = {}
    returnDict['success'] = -1
    objectID = request.POST.get("objectID", "")
    return check_user_id(objectID)

def check_user_id_exists(objectId):
    if check_user_id(objectId)['success'] == 1:
        return True
    return False

def check_user_id(objectID):
    '''
    Checks to see if the user id is valid
    :param objectID:
    :param returnDict:
    :return:
    '''
    returnDict = {}
    try:
        checkForUser = User.objects.get(id=objectID)
        returnDict['success'] = 1
        returnDict['message'] = 'objectID exists!'
        returnDict['email'] = checkForUser.email

        return returnDict

    except User.DoesNotExist:
        returnDict['success'] = 0
        returnDict['message'] = 'objectID does not exist'
        return returnDict

def get_user(objectID, emailString):
    '''
    Returns the user object
    :param objectID: objectID to look for
    :param emailString: email to look for
    :return: user object (or none if it does not exist)
    '''
    try:
        checkForUser = User.objects.get(id=objectID, email=emailString)
        return checkForUser
    except User.DoesNotExist:
        return None

def check_user_id_and_email(objectID, emailString):
    returnDict = {}
    try:
        checkForUser = User.objects.get(id=objectID, email=emailString)
        returnDict['success'] = 1
        returnDict['message'] = 'objectID exists!'
        returnDict['email'] = checkForUser.email

        return returnDict

    except User.DoesNotExist:
        returnDict['success'] = 0
        returnDict['message'] = 'objectID does not exist'
        return returnDict
