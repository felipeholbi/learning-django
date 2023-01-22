from django.db import models

# Create your models here.
class Pet(models.Model):
    SEX_CHOICE = [
        ('F', 'Female'),
        ('M', 'Male'),
    ]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True)
    description = models.TextField(blank=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICE, blank=True)
    submission_date = models.DateTimeField()
    age = models.IntegerField()
    vaccinations = models.ManyToManyField('Vaccine', blank=True)

class Vaccine(models.Model):
    name = models.CharField(max_length=50)
