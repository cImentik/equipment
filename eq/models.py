# -*- coding: utf-8 -*-
from datetime import date
from django.db import models


class Units(models.Model):
    unit = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.unit


class Employees(models.Model):
    surname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    hired = models.DateField(default=date.today())
    moved = models.DateField(default=date.today())
    unit = models.ForeignKey(Units)

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

    def __str__(self):
        return self.group_name


class Constructions(models.Model):
    group_name = models.ForeignKey(TypeEquipments)
    constructons_name = models.CharField(max_length=20)

    def __str__(self):
        return self.constructons_name


class Equipments(models.Model):
    type_eq = models.ForeignKey(TypeEquipments)
    model_name = models.CharField(max_length=20)     #название модели
    manufacturer = models.CharField(max_length=20)   #производитель
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2) #цена
    life = models.FloatField(default=0.0)            #срок службы
    #
    construction = models.ForeignKey(Constructions)  #конструкция
    shockproof = models.NullBooleanField(null=True)  #от удара
    insulation = models.NullBooleanField(null=True)  #шумоизоляция
    laser = models.NullBooleanField(null=True)       #лазер
    ir_radiation = models.NullBooleanField(null=True)#ИК
    yf_radiation = models.NullBooleanField(null=True)#УФ
    l_radiaton =  models.NullBooleanField(null=True) #световое излучение
    air_temp = models.FloatField(default=0.0)        #температура воздуха
    sur_temp = models.FloatField(default=0.0)        #температура поверхности

    #TODO: дописать модель

    def __str__(self):
        return self.model_name


class Ownership(models.Model):
    equipment = models.ForeignKey(Equipments)
    employees = models.ForeignKey(Employees)
    #code_eq =
    delivery = models.DateField(default=date.today())

    def __str__(self):
        return self.employees.surname + ' ' + self.equipment.model_name