from django.db import models

class Login(models.Model):
    username=models.CharField(max_length=40)
    password=models.CharField(max_length=40)
