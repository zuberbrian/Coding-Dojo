from __future__ import unicode_literals
from django.db import models
import bcrypt
import re

emailRegex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
passwordRegex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')

# Create your models here.
class UserManager(models.Manager):
    def validation(self, postData):
        errors = {}
        if len(postData['first_name']) <= 2:
            errors['first_name'] = "First name must be longer than 2 characters, consult your dumb parents."
        elif not re.match('[A-Za-z]+', postData['first_name']):
            errors['first_name'] = "First name may only contain letters."
        if len(postData['last_name']) <= 2:
            errors['last_name'] = "Last name must be longer than 2 characters, consult Ellis Island."
        elif not re.match('[A-Za-z]+', postData['last_name']):
            errors['last_name'] = "Last name may only contain letters."
        if len(postData['email']) <=2:
            errors['email'] = "Please provide a valid email address."
        elif User.objects.filter(email=postData['email']):
            errors['email'] = "Email has already been registered."
        elif not re.match('[A-Za-z0-9-_]+(.[A-Za-z0-9-_]+)*@[A-Za-z0-9-]+(.[A-Za-z0-9]+)*(.[A-Za-z]{2,})',postData['email']):
            errors['email'] = "Incorrect email format."
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters."
        elif postData['pw_confirm'] != postData['password']:
            errors['password'] = "Passwords do not match."
        if len(errors):
            result = {
                'errors' : errors
            }
        else:
            pwhash = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            user = self.create(first_name=postData['first_name'], last_name=postData['last_name'], email=postData['email'], password=pwhash)
            result = {
                'new_users' : user
            }
        return result
    def login_validation(self, postData):
        errors = {}
        if len(postData['email']) < 1:
            errors['loginemail'] = "Please enter your email."
        elif not User.objects.filter(email=postData['email']):
            errors['loginemail'] = "Email not found."
        elif len(postData['password']) < 1:
            errors['loginpass'] = "Please enter your password."
        elif not bcrypt.checkpw(postData['password'].encode(), User.objects.get(email=postData['email']).password.encode()):
            errors['loginpass'] = "Incorrect password."
        if len(errors):
            result = {
                'errors' : errors
            }
        else:
            result = {
                'message' : "Success!"
            }
        return result

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class Job(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    addedby = models.ForeignKey(User, related_name="added_by")
    user_joblist = models.ManyToManyField(User, related_name="joblist")