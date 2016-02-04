from requestJob.models import JobRequest
from login.loginHelper import check_user_id_and_email
from mongoengine.fields import *


def submitJobRequest( request ):
    '''
    
    :param request:
    :return:
    '''

    userIdPost = request.POST.get('userId','')
    emailPost = request.POST.get('email', '')
    descriptionPost = request.POST.get('description', '')
    userSubmitPrice = request.POST.get('userSubmitPrice', '')

    if check_user_id_and_email(userIdPost, emailPost)['success'] == 1:
        return submit_job_request(userIdPost, emailPost, descriptionPost, userSubmitPrice)

    else:
        returnDict = {}
        returnDict['success'] = -1
        returnDict['message'] = 'User does not exist!'
        return returnDict


def submit_job_request(user_id_post, email_post, description_post, user_submit_price):
    '''

    :param user_id_post:
    :param email_post:
    :param description_post:
    :param user_submit_price:
    :return:
    '''
    job_to_add = JobRequest(userId=user_id_post, email=email_post, stillSearching=True)
    from datetime import datetime
    job_to_add.timeOfRequest = datetime.now()
    job_to_add.userSubmitPrice = int(user_submit_price)
    job_to_add.description = description_post
    job_to_add.listOfBidders = [StringField('testing'), StringField(user_id_post)]
    job_to_add.listOfBids = [IntField(10), IntField(11)]
    job_to_add.save()

    returnDict = {}
    returnDict['success'] = 1
    returnDict['message'] = 'Job request successful'
    return returnDict