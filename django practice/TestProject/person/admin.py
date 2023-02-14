from django.contrib import admin
from person.models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display=('person_name','person_age','person_phone','person_desc','person_img')
admin.site.register(Person,PersonAdmin)

# Register your models here.
