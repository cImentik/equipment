# -*- coding: utf-8 -*-
from datetime import date
from django.db import models


class Professions(models.Model):
    name = models.CharField('должность', max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"


class Units(models.Model):
    unit = models.CharField('отдел', max_length=50, blank=True, null=True)

    def __str__(self):
        return self.unit

    class Meta:
        verbose_name = "Подразделение"
        verbose_name_plural = "Подразделения"


class Employees(models.Model):
    surname = models.CharField('фамилия', max_length=50)
    firstname = models.CharField('имя', max_length=50)
    patronymic = models.CharField('отчество', max_length=50)
    #profession = models.CharField('должность', max_length=50, default='')
    tabel_num = models.CharField('табельный номер', max_length=10, default='')
    hired = models.DateField('принят', default=date.today())
    moved = models.DateField('перемещён', default=date.today())
    unit = models.ForeignKey(Units)

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def fio(self):
        return self.surname + ' ' + self.firstname[0] + '. ' + self.patronymic[0] + '.'

    def __str__(self):
        return self.surname + ' ' + self.firstname[0] + '. ' + self.patronymic[0] + '.'


class Anthropometry(models.Model):
    head_around = models.SmallIntegerField('окружность головы')
    face_around = models.SmallIntegerField('окружность лица')
    growth = models.SmallIntegerField('рост')
    chest = models.SmallIntegerField('обхват груди')

    class Meta:
        verbose_name = "Антропометрия"
        verbose_name_plural = "Антропометрия"


class Proportions(models.Model):
    dress = models.SmallIntegerField()
    pants = models.SmallIntegerField()
    hat = models.SmallIntegerField()
    gas_mask = models.SmallIntegerField()
    glasses = models.SmallIntegerField()
    height_size = models.SmallIntegerField()
    shoes = models.SmallIntegerField()

    class Meta:
        verbose_name = "Размеры"
        verbose_name_plural = "Размеры"


class TypeEquipments(models.Model):
    group_name = models.CharField('тип экиперовки', max_length=20)

    def __str__(self):
        return self.group_name

    class Meta:
        ordering = ["group_name"]
        verbose_name = "тип экиперовки"
        verbose_name_plural = "типы экипировки"


class Constructions(models.Model):
    group_name = models.ForeignKey(TypeEquipments)
    constructons_name = models.CharField('конструкция', max_length=20)

    def __str__(self):
        return self.constructons_name

    class Meta:
        verbose_name = "конструкция"
        verbose_name_plural = "конструкции"


class Equipments(models.Model):
    type_eq = models.ForeignKey(TypeEquipments)
    model_name = models.CharField('модель', max_length=20)     #название модели
    manufacturer = models.CharField('производитель', max_length=20)   #производитель
    price = models.DecimalField('цена', default=0.00, max_digits=7, decimal_places=2) #цена
    life = models.FloatField('срок службы', default=0.0)            #срок службы
    catalog_num = models.CharField('каталожный номер', max_length=10, default='')   #каталожный номер
    #
    construction = models.ForeignKey(Constructions)  #конструкция
    shockproof = models.NullBooleanField('интиударный', null=True)  #от удара
    insulation = models.NullBooleanField('шумоизоляция', null=True)  #шумоизоляция
    laser = models.NullBooleanField('лазер', null=True)       #лазер
    ir_radiation = models.NullBooleanField('ИК', null=True)#ИК
    yf_radiation = models.NullBooleanField('УФ', null=True)#УФ
    l_radiaton =  models.NullBooleanField('световое излучение', null=True) #световое излучение
    air_temp = models.FloatField('температура воздуха', default=0.0)        #температура воздуха
    sur_temp = models.FloatField('температура поверхности', default=0.0)        #температура поверхности

    #TODO: дописать модель

    def __str__(self):
        return self.model_name

    class Meta:
        verbose_name = "СИЗ"
        verbose_name_plural = "Экипировка"


class Ownership(models.Model):
    equipment = models.ForeignKey(Equipments)
    employees = models.ForeignKey(Employees)
    #code_eq =
    delivery = models.DateField('выдано', default=date.today()) #дата получения (выдачи)

    def is_expend(self, equipment_life):
        # if
        return True

    def __str__(self):
        return self.employees.surname + ' ' + self.equipment.model_name

    class Meta:
        verbose_name = "Выдано"
        verbose_name_plural = "Выдано"