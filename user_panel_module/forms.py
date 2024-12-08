from django import forms
from patient_module.models import Patient



class EditProfileModelForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['username','first_name','last_name', 'phonenumber', 'age', 'address', 'information', 'gender','file']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'نام کاربری',
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder':'نام',
                    'maxlength': '50',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'نام خانوادگی',
                    'maxlength': '50',

                }
            ),
            'phonenumber': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'شماره تماس',
                    'maxlength': '11',

                }
            ),
            'age': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'سن',
                    'maxlength': '2',
                }
            ),
            'file': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'ارسال فایل'
                }
            ),
            'address': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'آدرس منزل',
                    'maxlength': '150',
                }
            ),

            'information': forms.CheckboxSelectMultiple(),
            'gender': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            )

        }
        error_messages = {
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