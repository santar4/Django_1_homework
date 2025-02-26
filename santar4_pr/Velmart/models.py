from django.db import models


class Worker(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    male = models.CharField(max_length=50)
    age = models.IntegerField()
    birthdate = models.DateField()
    jop_position = models.CharField(max_length=150)
    phone_number = models.IntegerField()







