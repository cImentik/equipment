from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from eq.models import Ownership, Equipments, Employees

# Create your views here.


def index(request):
    return HttpResponse("OOOps...")


def cart(request, employe_id):
    ownerships = Ownership.objects.filter(employees_id=employe_id)
    if len(ownerships) > 0:
        employee = ownerships[0].employees
    else:
        raise Http404
    context = {'ownerships': ownerships, 'employee': employee}
    return render(request, 'eq/cart.html', context)


def empl(request):
    return HttpResponse("Get me employees...")
