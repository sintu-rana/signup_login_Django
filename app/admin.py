from django.contrib import admin
from app.models import CustomUser,TODO, Manager, Employee

# Register your models here.

admin.site.register(CustomUser)

admin.site.register(TODO)

admin.site.register(Manager)

admin.site.register(Employee)


