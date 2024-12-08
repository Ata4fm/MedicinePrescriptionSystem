from django import forms
from .models import Patient



class AddPatientModelForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['code','username','first_name','last_name','password', 'phonenumber', 'age', 'address', 'information', 'gender']
        widgets = {
            'code': forms.TextInput(
                attrs={
                'class': 'form-control',
                'placeholder':'کد ملی'
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'نام کاربری'
                }
            ),
            'password': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'گذرواژه'
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'نام'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'نام خانوادگی'

                }
            ),
            'phonenumber': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'شماره تماس'
                }
            ),
            'age': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'سن'
                }
            ),

            'address': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'آدرس منزل'
                }
            ),

            'information': forms.CheckboxSelectMultiple()

        }

        error_messages = {
            'code': {
                'required': 'لطفا کد ملی را وارد نمایید',
                'max_length': 'لطفا بیشتر از تعداد 10 وارد نکنید'
            },
            'username': {
                'required': 'لطفا نام کاربری را وارد نمایید',
                'max_length': 'لطفا بیشتر از تعداد 100 وارد نکنید'
            },
            'first_name': {
                'required': 'لطفا نام را وارد نمایید',
                'max_length': 'لطفا بیشتر از تعداد 100 وارد نکنید'
            },
            'last_name': {
                'required': 'لطفا نام خانوادگی را وارد نمایید',
                'max_length': 'لطفا بیشتر از تعداد 100 وارد نکنید'
            },
            'password': {
                'required': 'لطفا گذرواژه را وارد نمایید',
                'max_length': 'لطفا بیشتر از تعداد 50 وارد نکنید'
            },
            'phonenumber': {
                'required': 'لطفا شماره تماس را وارد نمایید',
                'max_length': 'لطفا بیشتر از تعداد 11 وارد نکنید'
            },
            'age': {
                'required': 'لطفا سن را وارد نمایید',
                'max_length': 'لطفا بیشتر از تعداد 10 وارد نکنید'
            },
            'address': {
                'required': 'لطفا آدرس محل زندگی را وارد نمایید',
                'max_length': 'لطفا بیشتر از تعداد 100 وارد نکنید'
            },
            'information': {
                'required': 'لطفا یکی از گزینه را انتخاب نمایید',
            },
            'gender': {
                'required': 'لطفا جنسیت بیمار را را وارد نمایید',
            },
        }