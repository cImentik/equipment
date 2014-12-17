from datetime import date
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


class TypeEquipments(models.Model):
    group_name = models.CharField(max_length=20)


class Constructions(models.Model):
    group_name = models.ForeignKey(TypeEquipments)
    constructons_name = models.CharField(max_length=20)


class Equipments(models.Model):
    type_eq = models.ForeignKey(TypeEquipments)
    model_name = models.CharField(max_length=20)
    manufacturer = models.CharField(max_length=20)
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    life = models.FloatField(default=0.0)
    #
    construction = models.ForeignKey(Constructions)
    shockproof = models.NullBooleanField(null=True, default=None)  #противоудар
    insulation = models.NullBooleanField(null=True, default=None)  #шумоизоляция
    #TODO: дописать модель


class Ownership(models.Model):
    equipment = models.ForeignKey(Equipments)
    employees = models.ForeignKey(Employees)
    #code_eq =
    delivery = models.DateField(default=date.today())