from requestJob.models import job_search
from login.loginHelper import check_user_id_and_email
from mongoengine.fields import *


def submit_job_search( request ):
    '''
    
    :param request:
    :return:
    '''

    userIdPost = request.POST.get('userId','')
    emailPost = request.POST.get('email', '')
    userRequestPrice = request.POST.get('userRequestPrice', '')
    jobCategory = request.POST.get('jobCategory', '')

    if check_user_id_and_email(userIdPost, emailPost)['success'] == 1:
        return submit_job_request(userIdPost, emailPost, userRequestPrice, jobCategory)

    else:
        returnDict = {}
        returnDict['success'] = -1
        returnDict['message'] = 'User does not exist!'
        return returnDict


def submit_job_request(user_id_post, email_post, userRequestPrice, jobCategory):
    '''

    :param user_id_post:
    :param email_post:
    :param description_post:
    :param user_submit_price:
    :return:
    '''
    jobSearchToAdd = job_search(userId=user_id_post, email=email_post, stillSearching=True)
    from datetime import datetime
    jobSearchToAdd.timeOfRequest = datetime.now()
    jobSearchToAdd.userRequestPrice = int(userRequestPrice)
    jobSearchToAdd.jobCategory = jobCategory
    jobSearchToAdd.save()

    returnDict = {}
    returnDict['success'] = 1
    returnDict['message'] = 'Job request successful'
    return returnDict
