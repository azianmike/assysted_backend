from requestJob.helper_func import create_return_dict
from requestJob.models import job_search
from login.loginHelper import check_user_id_and_email, get_user
from requestJob.job_categories import is_valid_category

def invalid_price( price ):
    if price<10 or price >1000:
        return True
    return False

def submitJobSearch( request ):
    '''
    
    :param request:
    :return:
    '''

    userIdPost = request.POST.get('userId','')
    emailPost = request.POST.get('email', '')
    userRequestPrice = request.POST.get('userSearchPrice', '')
    jobCategory = request.POST.get('jobCategory', '')

    checkUser = get_user(userIdPost, emailPost)

    if invalid_price( int(userRequestPrice) ):
        return create_return_dict(-1, 'Invalid request price')

    if checkUser is not None:
        if is_valid_category(jobCategory):
            return submit_job_search(userIdPost, emailPost, userRequestPrice, jobCategory, checkUser)
        else:
            return create_return_dict(-1, 'Invalid job category')
    else:
        return create_return_dict(-1,'User does not exist!' )


def submit_job_search(user_id_post, email_post, userRequestPrice, jobCategory, user):
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
    jobSearchToAdd.userAvgRating = user.avgRating
    jobSearchToAdd.userNumRating = user.numRatings
    jobSearchToAdd.save()

    returnDict = {}
    returnDict['success'] = 1
    returnDict['message'] = 'Job request successful'
    return returnDict
