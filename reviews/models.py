from mongoengine import connect, document
from mongoengine.fields import *

connect('assysted_DB')

class Rating(document.Document):
    #person submitting the review
    reviewer = ObjectIdField(required=True)
    #person BEING reviewed
    userBeingReviewed = ObjectIdField(required=True)
    rating = IntField(required=True, min_value=0, max_value=5)
    description = StringField(required=True, default='')