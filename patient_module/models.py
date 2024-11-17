from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator
from django.db import models

# Create your models here.

class PatientHealthyInformation(models.Model):
    title = models.CharField(max_length=100,verbose_name='اطلاعات بیماری مریض')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'سوابق سلامتی بیمار'
        verbose_name_plural = 'سوابق سلامتی بیماران'

class PatientGender(models.Model):
    title = models.CharField(max_length=100,verbose_name='جنسیت')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'جنسیت بیمار'
        verbose_name_plural = 'جنسیت بیماران'




class Patient(AbstractUser):

    code = models.CharField(max_length=10, unique=True,null=False, verbose_name='کد ملی')
    phonenumber = models.CharField(max_length=11, verbose_name='شماره تلفن',validators=[MaxLengthValidator(11)])
    age = models.CharField(max_length=5,verbose_name='سن', null=True, blank=True)
    address = models.CharField(max_length=100, verbose_name='آدرس',null=True, blank=True)
    information = models.ManyToManyField(PatientHealthyInformation,default='موردی ندارم',null=True,blank=True,verbose_name='اطلاعات سوابق بیماری')
    gender = models.ForeignKey(PatientGender, on_delete=models.CASCADE, null=True, blank=True,verbose_name='جنسیت')
    file = models.FileField(upload_to='patients/',verbose_name='آپلود فایل',null=True, blank=True)


    def __str__(self):
        return f'{self.code} - {self.phonenumber}'

    class Meta:
        verbose_name = 'بیمار'
        verbose_name_plural = 'بیماران'

