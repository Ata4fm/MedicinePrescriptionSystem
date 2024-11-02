from django import forms
from .models import Patient



class AddPatientModelForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['code', 'firstname', 'lastname', 'phonenumber', 'age', 'address', 'information', 'gender']

        widgets = {
            'code': forms.TextInput(
                attrs={
                'class': 'form-control',
                'placeholder':'کد ملی'
                }
            ),
            'firstname': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'نام'
                }
            ),
            'lastname': forms.TextInput(
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
            'firstname': {
                'required': 'لطفا نام را وارد نمایید',
                'max_length': 'لطفا بیشتر از تعداد 100 وارد نکنید'
            },
            'lastname': {
                'required': 'لطفا نام خانوادگی را وارد نمایید',
                'max_length': 'لطفا بیشتر از تعداد 100 وارد نکنید'
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