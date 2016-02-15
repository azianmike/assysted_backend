from requestJob.models import job_request
from login.loginHelper import check_user_id_and_email
from mongoengine.fields import *
from requestJob.job_categories import is_valid_category
from requestJob.helper_func import create_return_dict

def submitJobRequest( request ):
    '''
    
    :param request:
    :return:
    '''

    userIdPost = request.POST.get('userId','')
    emailPost = request.POST.get('email', '')
    descriptionPost = request.POST.get('description', '')
    userSubmitPrice = request.POST.get('userSubmitPrice', '')
    jobCategory = request.POST.get('jobCategory', '')

    if check_user_id_and_email(userIdPost, emailPost)['success'] == 1:
        if is_valid_category(jobCategory):
            return submit_job_request(userIdPost, emailPost, descriptionPost, userSubmitPrice, jobCategory)
        else:
            return create_return_dict(-1, 'Invalid job category')
    else:
        return create_return_dict(-1, 'User does not exist!')


def submit_job_request(user_id_post, email_post, description_post, user_submit_price, job_category):
    '''

    :param user_id_post:
    :param email_post:
    :param description_post:
    :param user_submit_price:
    :return:
    '''
    job_to_add = job_request(userId=user_id_post, email=email_post, stillSearching=True)
    from datetime import datetime
    job_to_add.timeOfRequest = datetime.now()
    job_to_add.userSubmitPrice = int(user_submit_price)
    job_to_add.description = description_post
    job_to_add.listOfBidders = [{user_id_post:email_post}, {user_id_post:'testing'}]
    job_to_add.listOfBids = [10, 11]
    job_to_add.jobCategory = job_category
    job_to_add.save()

    returnDict = {}
    returnDict['success'] = 1
    returnDict['message'] = 'Job request successful'
    return returnDict
