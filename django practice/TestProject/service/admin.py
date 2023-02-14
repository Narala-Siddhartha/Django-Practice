from django.contrib import admin
from service.models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display=('Name','Age','Phone')
admin.site.register(Service,ServiceAdmin)
# Register your models here.
