from django.db import models


class OTP(models.Model):
    phone = models.CharField(max_length=11,verbose_name="شماره تماس")
    code = models.CharField(max_length=6,verbose_name="کد تایید")
    expiration_date = models.DateTimeField(auto_now_add=True)



    class Meta:
        verbose_name = 'کد احراز هویت'
        verbose_name_plural = 'کد های احراز هویت'

    def __str__(self):
        return f'{self.phone} {self.code}'