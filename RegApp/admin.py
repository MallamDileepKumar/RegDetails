from django.contrib import admin
from .models import Registration
# Register your models here.

class RegAdmin(admin.ModelAdmin):
    list_display = ['username','email','password','conform_password']

admin.site.register(Registration,RegAdmin)
