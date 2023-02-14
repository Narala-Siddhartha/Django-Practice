from django.db import models

class SaveFormData(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.CharField(max_length=40)
    Website = models.CharField(max_length=50)
    Message = models.TextField()
