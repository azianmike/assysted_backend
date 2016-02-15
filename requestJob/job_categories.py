__author__ = 'michaell'

job_categories_list = ['copywriting', 'data entry', 'social media', 'event planning', 'transcription']
job_categories_dict = {'copywriting': True, 'data entry': True, 'social media': True, 'event planning': True,
                       'transcription': True}


def is_valid_category(category_to_check):
    return job_categories_dict.has_key(category_to_check)


def get_categories():
    return job_categories_list
