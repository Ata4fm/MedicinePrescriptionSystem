from django import forms
from django.core import validators

class LoginForm(forms.Form):
    code = forms.CharField(
        label='کد ملی',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'کد ملی',
                'maxlength': '10',
            }
        ),
        validators=[
            validators.MaxLengthValidator(10),
        ],
        error_messages={
            'required': 'لطفا کد ملی را وارد نمایید',
            'maxlength': 'تعداد بیشتر از 10 رقم وارد نمایید'
        }
    )

class CheckOTPForm(forms.Form):
    otp = forms.CharField(
        label='کد ارسالی',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'کد تایید پیامک',
                'maxlength': '6',
            }
        ),
        validators=[
            validators.MaxLengthValidator(10),
        ],
        error_messages={
            'required': 'لطفا کد تایید را وارد نمایید',
            'maxlength': 'تعداد بیشتر از 6 رقم وارد نمایید'
        }
    )
