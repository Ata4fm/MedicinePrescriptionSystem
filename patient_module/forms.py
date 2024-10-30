from django import forms
from django.db.models import CharField
from . import models
from .models import Patient


# class AddPatientForm(forms.Form):
#     code = forms.CharField(label='کد ملی',
#                            max_length=10,
#                            error_messages={
#                                'required': 'لطفا کد ملی را وارد نمایید',
#                                'max_length': 'لطفا بیشتر از تعداد 10 وارد نکنید'
#                            },
#                            widget=forms.TextInput(attrs={
#                                'class': 'form-control',
#                                'placeholder': 'کد ملی',
#                            })
#                            )
#
#     firstname = forms.CharField(label='نام',
#                                 max_length=50,
#                                 error_messages={
#                                     'required': 'لطفا نام را وارد نمایید',
#                                     'max_length': 'لطفا بیشتر از تعداد 50 وارد نکنید'
#                                 },
#                                 widget=forms.TextInput(attrs={
#                                     'class': 'form-control',
#                                     'placeholder': 'نام'
#
#                                 }))
#
#     lastname = forms.CharField(label='نام خانوادگی',
#                                max_length=50,
#                                error_messages={
#                                    'required': 'لطفا نام خانوادگی را وارد نمایید',
#                                    'max_length': 'لطفا بیشتر از تعداد 50 وارد نکنید'
#                                },
#
#                                widget=forms.TextInput(attrs={
#                                    'class': 'form-control',
#                                    'placeholder': 'نام خانوادگی'
#
#                                }))
#
#     phonenumber = forms.CharField(label='شماره تماس',
#                                   max_length=10,
#                                   error_messages={
#                                       'required': 'لطفا شماره تماس را وارد نمایید',
#                                       'max_length': 'لطفا بیشتر از تعداد 50 وارد نکنید'
#                                   },
#
#                                   widget=forms.TextInput(attrs={
#                                       'class': 'form-control',
#                                       'placeholder': 'شماره تماس'
#
#                                   }))
#     age = forms.CharField(label='سن',
#                           max_length=50,
#                           error_messages={
#                               'required': 'لطفا سن را وارد نمایید',
#                               'max_length': 'لطفا بیشتر از تعداد 50 وارد نکنید'
#                           },
#                           widget=forms.TextInput(attrs={
#                               'class': 'form-control',
#                               'placeholder': 'سن'
#
#                           }))
#     address = forms.CharField(label='آدرس',
#                               max_length=50,
#                               error_messages={
#                                   'required': 'لطفا آدرس را وارد نمایید',
#                                   'max_length': 'لطفا بیشتر از تعداد 50 وارد نکنید'
#                               },
#                               widget=forms.TextInput(attrs={
#                                   'class': 'form-control',
#                                   'placeholder': 'آدرس'
#
#                               }))
#     information = forms.ModelMultipleChoiceField(
#                                 label='سوابق بیماری',
#                                 queryset=models.PatientHealthyInformation.objects.all(),
#                                 widget=forms.CheckboxSelectMultiple())
#
#     gender = forms.ModelChoiceField(
#                                label='جنسیت',
#                                queryset=models.PatientGender.objects.all(),
#                                error_messages={
#                                    'required': 'لطفا جنسیت را وارد نمایید',
#                                },
#                                widget=forms.Select(attrs={
#                                    'class': 'form-select',
#                                }))


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
            # 'information': forms.ModelMultipleChoiceField(
            #     queryset=models.PatientHealthyInformation.objects.all(),
            #     widget=forms.CheckboxSelectMultiple()
            # ),
            'address': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'آدرس منزل'
                }
            ),

            'gender': forms.ModelChoiceField(
                queryset=models.PatientGender.objects.all(),
                widget=forms.Select(attrs={
                    'class': 'form-select',
                })
            )

        }