from django.contrib import admin

from .models import Prescription , PrescriptionDetails


# Register your models here.
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ['doctor','patient','created_date','is_submitted']


class PrescriptionAdminDetail(admin.ModelAdmin):
    list_display = ['prescription','medicine']


admin.site.register(Prescription,PrescriptionAdmin)
admin.site.register(PrescriptionDetails,PrescriptionAdminDetail)