from django.db import models

# Create your models here.
class Show(models.Model):
    name=models.CharField(max_length=100)
    watched=models.BooleanField
    genre=models.CharField(max_length=100)