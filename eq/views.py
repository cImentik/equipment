from django.shortcuts import render, redirect, render_to_response
from django.http import Http404
from datetime import date, timedelta
from eq.models import Ownership, Equipments, Employees, TypeEquipments, Units
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.db.models import F
from eq.forms import AddEmployeeForm, AddEquipmentForm

from django.http import HttpResponse

# Create your views here.

#@login_required
def master(request, unit_id=1):
    """Главная страница"""
    # if request.user.groups.get().name != 'master':
    #     return redirect('/')
    try:
        unit_name = Units.objects.get(pk=unit_id)
    except Units.DoesNotExist:
        raise Http404
    employees = Employees.objects.filter(unit__id=unit_id)
    context = {"employees": employees, "unit_name": unit_name}
    return render(request, 'eq/i_list.html', context)


#@permission_required('eq.', login_url="eq/login")
def cart(request, employe_id):
    """Учётная карточка работника"""
    user = auth.get_user(request)

    ownerships = Ownership.objects.filter(employees_id=employe_id)
    type_equipments = TypeEquipments.objects.all()
    if ownerships:
        employee = ownerships[0].employees
    else:
        raise Http404
    context = {
        'ownerships': ownerships,
        'employee': employee,
        'type_equipments': type_equipments,
        'employe_id': employe_id}
    return render(request, 'eq/cart.html', context)


def expend_list(request, unit_id=1, date_expend=date.today()):
    """ Список СЗ на списание """
    table_rows = []
    ownerships = Ownership.objects.filter(employees__unit__id=unit_id).order_by('employees__surname')  #.filter((F('equipment__life')+F('delivery'))==date_expend)
    for ownership in ownerships:
        time_life = ownership.delivery+timedelta(days=(ownership.equipment.life*365))
        if time_life <= date_expend:
            line = {'fio': ownership.employees.fio(),
                    'construction': ownership.equipment.construction.constructons_name,
                    'type': ownership.equipment.type_eq.group_name,
                    'manufacturer': ownership.equipment.manufacturer,
                    'expends': time_life,
                    }
            table_rows.append(line)

    context = {
        'date_expend': date_expend.strftime('%d.%m.%Y'),
        'table': table_rows,
    }
    return render_to_response('eq/expends.html', context)


def expend(request, unit_id, type_id):
    """ Конкретный тип экипировки"""
    context = {}
    return render_to_response('eq/expend.html', context)


def instock_list(request, unit_id=1):
    """ Список СЗ находящихся на руках """
    table_rows = []
    ownerships = Ownership.objects.filter(employees__unit__id=unit_id).order_by('employees__surname')
    for ownership in ownerships:
        line = {'fio': ownership.employees.fio(),
                'construction': ownership.equipment.construction.constructons_name,
                'type': ownership.equipment.type_eq.group_name,
                'manufacturer': ownership.equipment.manufacturer,
                }
        table_rows.append(line)

    context = {
        'table': table_rows,
    }
    return render_to_response('eq/instock.html', context)


def login(request):
    context = {}
    context.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('/')
        else:
            context['login_error'] = 1
            return render(request, 'eq/login.html', context)
    else:
        return render(request, 'eq/login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('eq/login')


def main(request):
    # try:
    #     user = auth.get_user(request)
    #     if user.groups.get().name == 'master':
    #         return redirect('master')
    #     elif user.groups.get().name == 'safetyeng':
    #         return redirect('safetyeng')
    #     elif user.groups.get().name == 'stockman':
    #         return redirect('stockman')
    #     elif user.groups.get().name == 'buh':
    #         return redirect('buh')
    #     else:
    #         return redirect('login')
    # except:
    #     return redirect('login')
    return HttpResponse("Hello")


def safetyeng(request):
    """Главная страница инженера по ТБ"""
    # if request.user.groups.get().name != 'master':
    #     return redirect('/')
    unit_name = "Инженер по ТБ"
    employees = Employees.objects.all()
    context = {"employees": employees, "unit_name": unit_name}
    return render(request, 'eq/i_list.html', context)


def stock(request):
    """Главная страница кладовщика"""
    # if request.user.groups.get().name != 'master':
    #     return redirect('/')
    unit_name = "Склад"
    employees = Employees.objects.all()
    context = {"employees": employees, "unit_name": unit_name}
    return render(request, 'eq/s_list.html', context)


def addempl(request):
    if request.method == 'POST':
        addForm = AddEmployeeForm(request.POST)
        if addForm.is_valid():
            addForm.save()
            return redirect('/')
    else:
        addForm = AddEmployeeForm()
        context = {"addForm": addForm}
        return render(request, 'eq/addempl.html', context)


def delempl(request):
    return None


def editempl(request):
    return None


def cartprint(request, employe_id):
    #assert False
    # try:
    #     unit_name = Units.objects.get(pk=unit_id)
    # except Units.DoesNotExist:
    #     raise Http404
    employe = Employees.objects.get(pk=employe_id)
    ownerships = Ownership.objects.filter(employees_id=employe_id)
    context = {"employe": employe,
               "ownerships": ownerships}
    return render(request, 'eq/cartprint.html', context)


def balance(request):
    equipments = Equipments.objects.all()
    context = {"equipments": equipments}
    return render(request, 'eq/stocklist.html', context)


def addeq(request):
    if request.method == 'POST':
        addItemForm = AddEquipmentForm(request.POST)
        if addItemForm.is_valid():
            addItemForm.save()
            return redirect('/balance/')
    else:
        addItemForm = AddEquipmentForm()
        context = {"addItemForm": addItemForm}
        return render(request, 'eq/additem.html', context)
