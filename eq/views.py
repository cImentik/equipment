from django.shortcuts import render, redirect, render_to_response
from django.http import Http404
from datetime import date, timedelta
from eq.models import Ownership, Equipments, Employees, TypeEquipments, Units
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.decorators import permission_required
from django.db.models import F

# Create your views here.


def index(request, unit_id=1):
    """Главная страница"""
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
        'type_equipments': type_equipments}
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
    return redirect ('eq/login')