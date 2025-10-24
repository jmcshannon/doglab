from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Breed(models.Model):

    SIZE_CHOICES = {
        'TINY': 'Tiny',
        'SMALL': 'SMALL',
        'MEDIUM': 'MEDIUM',
        'LARGE': 'LARGE'
    }
    name = models.CharField(max_length=50)
    size = models.CharField(choices=SIZE_CHOICES)
    friendliness = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    trainability = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    sheddingamount = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    exerciseneeds = models.PositiveIntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])


class Dog(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    color = models.CharField(max_length=20)
    favoritefood = models.CharField(max_length=20)
    favoritetoy = models.CharField(max_length=20)