from django.contrib import admin
from eq.models import Employees, Equipments, Anthropometry, Proportions, Ownership, TypeEquipments, Constructions
from eq.models import Units
# Register your models here.

admin.site.register(Employees)
admin.site.register(Equipments)
admin.site.register(Anthropometry)
admin.site.register(Proportions)
admin.site.register(Ownership)
admin.site.register(TypeEquipments)
admin.site.register(Constructions)
admin.site.register(Units)