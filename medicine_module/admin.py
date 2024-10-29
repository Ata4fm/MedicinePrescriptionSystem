from symtable import Class

from django.contrib import admin
from . import models

# Register your models here.


class MedicineCategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__','name']

class MedicineAdmin(admin.ModelAdmin):
    list_display = ['name','category','short_desc']
    list_filter = ['category']




admin.site.register(models.Medicine,MedicineAdmin)
admin.site.register(models.MedicineCategory,MedicineCategoryAdmin)