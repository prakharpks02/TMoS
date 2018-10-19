from django.db import models

class Home(models.Model):
    source = models.CharField(max_length=40)
    destination1 = models.CharField(max_length=40)
    destination2 = models.CharField(max_length=40)
    destination3 = models.CharField(max_length=40)
    destination4 = models.CharField(max_length=40)
    destination5 = models.CharField(max_length=40)
    destination6 = models.CharField(max_length=40)
    destination7 = models.CharField(max_length=40)
    destination8 = models.CharField(max_length=40)
    destination9 = models.CharField(max_length=40)
    destination10 = models.CharField(max_length=40)
    no_of_destinations = models.IntegerField()
