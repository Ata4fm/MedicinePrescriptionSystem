from django.contrib import admin
from . import models

# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    list_display = ['code','age','phonenumber']

class PatientInfoAdmin(admin.ModelAdmin):
    list_display = ['title']

class PatientGenderAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(models.Patient,PatientAdmin)
admin.site.register(models.PatientHealthyInformation,PatientInfoAdmin)
admin.site.register(models.PatientGender,PatientGenderAdmin)