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