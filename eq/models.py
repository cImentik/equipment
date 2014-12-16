from django.db import models

# Create your models here.


class Employees(models.Model):
    surname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    hired = models.DateField()
    moved = models.DateField()

    def __str__(self):
        return self.surname + ' ' + self.firstname


class Anthropometry(models.Model):
    head_around = models.SmallIntegerField()
    face_around = models.SmallIntegerField()
    growth = models.SmallIntegerField()
    chest = models.SmallIntegerField()


class Proportions(models.Model):
    dress = models.SmallIntegerField()
    pants = models.SmallIntegerField()
    hat = models.SmallIntegerField()
    gas_mask = models.SmallIntegerField()
    glasses = models.SmallIntegerField()
    height_size = models.SmallIntegerField()
    shoes = models.SmallIntegerField()