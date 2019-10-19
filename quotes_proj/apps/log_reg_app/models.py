from django.db import models


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = 'First name must be longer than two characters'
        if len(postData['last_name']) < 2:
            errors['last_name']= 'Last name must be longer than two characters'
        email = postData['email']
      
        if '@' not in email: 
            errors['email']= 'Must have a valid email, bro.'
        if '.com' not in email:
            errors['email']= 'Must have a valid email, bro.'
        if len(postData['password']) < 3:
            errors['password'] = 'Password must be at least 3 characters'
        if postData['password'] != postData['confirm_password']:
            errors['password'] = 'Passwords do not match!'
        return errors

class users(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=55)
    password = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    objects = UserManager()