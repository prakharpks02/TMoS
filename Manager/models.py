from django.db import models

class Home(models.Model):
    source=models.CharField(max_length=40)
    destination=models.CharField(max_length=40)

