from django.shortcuts import render
from django.http import HttpResponse
from eq.models import Ownership, Equipments

# Create your views here.


def index(request):
    return HttpResponse("OOOps...")


def cart(request, employe_id):
    ownerships = Ownership.objects.filter(employees_id=employe_id)

    response = ', '.join([p.equipment.model_name for p in ownerships])
    return HttpResponse(response)


def empl(request):
    return HttpResponse("Get me employees...")
