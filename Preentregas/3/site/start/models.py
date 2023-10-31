from django.db import models

class Dice(models.Model):
    style=models.CharField(max_length=40)
    faces=models.IntegerField()
    numbering=models.CharField(max_length=40)

class DiceBag(models.Model):
    material=models.CharField(max_length=40)
    color=models.CharField(max_length=40)
    capacity=models.IntegerField()
