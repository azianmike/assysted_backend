__author__ = 'michaell'

#only doing digital design for now
job_categories_list = ['digital design']
job_categories_dict = {'digital design': True}


def is_valid_category(category_to_check):
    return category_to_check in job_categories_dict


def get_categories():
    return job_categories_list
