from django.db import models

from medicine_module.models import Medicine
from patient_module.models import Patient


# Create your models here.

class Prescription(models.Model):
    doctor = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='نام پزشک',related_name='doctor',limit_choices_to={'is_superuser': True})
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,verbose_name='بیمار',related_name='patient',null=True,blank=True)
    is_submitted = models.BooleanField(verbose_name='نهایی شده/نشده')
    created_date = models.DateField(null=True,blank=True,verbose_name='تاریخ ایجاد نسخه')

    def __str__(self):
        return f'{self.doctor} {self.patient}'

    class Meta:
        verbose_name = 'نسخه دارو بیمار'
        verbose_name_plural = 'نسخه های دارو بیماران'

class PrescriptionDetails(models.Model):
    prescription = models.ForeignKey(Prescription,on_delete=models.CASCADE, verbose_name='نسخه دارو')
    medicine = models.ForeignKey(Medicine,on_delete=models.CASCADE, verbose_name='دارو')
    count = models.IntegerField(verbose_name='تعداد')

    def __str__(self):
        return f'{self.prescription}'

    class Meta:
        verbose_name = 'جزئیات نسخه دارو ها'
        verbose_name_plural = 'لیست جزئیات نسخه دارو'