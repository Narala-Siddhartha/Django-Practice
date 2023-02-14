from django.db import models
from tinymce.models import HTMLField

class Service(models.Model):
    Name = models.CharField(max_length=20)
    Age = models.CharField(max_length=3)
    Phone = models.CharField(max_length=10)

# Create your models here.
