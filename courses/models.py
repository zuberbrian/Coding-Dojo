from __future__ import unicode_literals
from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def validation(self, postData):
        errors = {}
        if len(postData['name']) <= 10:
            errors['name'] = "Course name must be at least 10 characters."
        if len(postData['descrip']) <= 15:
            errors['descrip'] = "Description must have at least 15 characters."
        
        if len(errors):
            result = {
                "errors": errors
            }
        else:
            course = self.create(name=postData['name'], descrip = postData['descrip'])

            result = {
                'new_course': course
            }
        return result
           
            
        

class Course(models.Model):
    name = models.CharField(max_length=255)
    descrip = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()