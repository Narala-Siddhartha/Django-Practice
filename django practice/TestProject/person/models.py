from django.db import models
from tinymce.models import HTMLField

class Person(models.Model):
    person_name = models.CharField(max_length=20)
    person_age = models.CharField(max_length=3)
    person_phone = models.CharField(max_length=10)
    person_desc = HTMLField()
    person_img = models.FileField(upload_to="person/",max_length=250,null=True,default=None)

# Create your models here.
