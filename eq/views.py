from django.shortcuts import render, redirect, render_to_response
from django.http import Http404
from django.http import HttpResponse
from eq.models import Ownership, Equipments, Employees, TypeEquipments, Units
from django.contrib import auth
from django.core.context_processors import csrf

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


def cart(request, employe_id):
    """Учётная карточка работника"""
    ownerships = Ownership.objects.filter(employees_id=employe_id)
    type_equipments = TypeEquipments.objects.all()
    if ownerships:
        employee = ownerships[0].employees
    else:
        raise Http404
    context = {'ownerships': ownerships, 'employee': employee, 'type_equipments': type_equipments}
    return render(request, 'eq/cart.html', context)


def empl(request):
    return HttpResponse("Get me employees...")


def login(request):
    context = {}
    context.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
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