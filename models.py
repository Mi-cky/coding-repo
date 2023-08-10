from django.db import models
# from django.contrib.auth.models import AbstractUserUser
# # # Create your models here.
class CustomUser(models.Model):
     
     username = models.CharField(max_length=100)
     fname = models.CharField(max_length=100)
     lname = models.CharField(max_length=100)

