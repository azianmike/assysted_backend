__author__ = 'michaell'


def create_return_dict(success_code, message):
    returnDict = {}
    returnDict['success'] = success_code
    returnDict['message'] = message
    return returnDict