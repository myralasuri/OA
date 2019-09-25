from django.contrib import admin

from employee.models import Employe, Department, Leaves, Position

# Register your models here.

admin.site.register(Employe)
admin.site.register(Department)
admin.site.register(Leaves)
admin.site.register(Position)