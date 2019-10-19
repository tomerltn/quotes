from django.db import models
from apps.log_reg_app.models import *

class QuotesManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['quote']) < 10:
            errors['quote'] = 'Quote needs more than 3 characters, brotato chip.'
        return errors 

class quotes(models.Model):
    quote = models.CharField(max_length=400)
    author = models.CharField(max_length=225)
    posted_by = models.ForeignKey(users, related_name="quotes_uploaded")
    users_who_like = models.ManyToManyField(users, related_name="liked_quotes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = QuotesManager()