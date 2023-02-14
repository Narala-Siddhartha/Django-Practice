from django.contrib import admin
from saveformdata.models import SaveFormData

class SaveFormDataAdmin(admin.ModelAdmin):
    list_display=("Name","Email","Website","Message")
admin.site.register(SaveFormData,SaveFormDataAdmin)
