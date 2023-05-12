from django.contrib import admin
from app.models import CustomUser,TODO

# Register your models here.

admin.site.register(CustomUser)

admin.site.register(TODO)

