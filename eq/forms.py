# -*- coding: utf-8 -*-
from django.forms import ModelForm
from eq.models import Employees


class AddEmployeeForm(ModelForm):
    class Meta:
        model = Employees
        fields = '__all__'


# class Employees(models.Model):
#     surname = models.CharField(max_length=50)
#     firstname = models.CharField(max_length=50)
#     patronymic = models.CharField(max_length=50)
#     profession = models.CharField(max_length=50, default='')
#     tabel_num = models.CharField(max_length=10, default='')
#     hired = models.DateField(default=date.today())
#     moved = models.DateField(default=date.today())
#     unit = models.ForeignKey(Units)