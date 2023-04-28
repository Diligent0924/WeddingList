from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    is_wedding = models.BooleanField(default= False)