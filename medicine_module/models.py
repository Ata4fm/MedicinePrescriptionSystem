from django.db import models

class MedicineCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام دسته بندی')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'دسته بندی دارو'
        verbose_name_plural = 'دسته بندی دارو ها'


class Medicine(models.Model):
    name = models.CharField(max_length=100,verbose_name='نام دارو')
    short_desc = models.CharField(max_length=100,verbose_name='توضیحات مصرف')
    category = models.ForeignKey(MedicineCategory,max_length=100,on_delete=models.CASCADE,null=True,verbose_name='دسته بندی')


    def __str__(self):
        return f'{self.name} {self.category} {self.short_desc}'

    class Meta:
        verbose_name = 'دارو'
        verbose_name_plural = 'دارو ها'
