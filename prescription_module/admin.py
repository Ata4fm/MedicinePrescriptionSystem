from django.contrib import admin

from .models import Prescription , PrescriptionDetails


# Register your models here.

admin.site.register(Prescription)
admin.site.register(PrescriptionDetails)