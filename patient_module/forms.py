from django import forms
from django.db.models import CharField


class AddPatientForm(forms.Form):
    code = forms.CharField(label='کد ملی',
                           max_length=10,
                           error_messages={
                               'required': 'لطفا کد ملی را وارد نمایید',
                               'max_length': 'لطفا بیشتر از تعداد 10 وارد نکنید'
                           },
                           widget=forms.TextInput(attrs={
                               'class': 'form-control',
                               'placeholder': 'کد ملی',
                           })
                           )

    firstname = forms.CharField(label='نام',
                                max_length=50,
                                error_messages={
                                    'required': 'لطفا نام را وارد نمایید',
                                    'max_length': 'لطفا بیشتر از تعداد 50 وارد نکنید'
                                },
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'نام'

                                }))

    lastname = forms.CharField(label='نام خانوادگی',
                               max_length=50,
                               error_messages={
                                   'required': 'لطفا نام خانوادگی را وارد نمایید',
                                   'max_length': 'لطفا بیشتر از تعداد 50 وارد نکنید'
                               },

                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'نام خانوادگی'

                               }))

    phonenumber = forms.CharField(label='شماره تماس',
                                  max_length=10,
                                  error_messages={
                                      'required': 'لطفا شماره تماس را وارد نمایید',
                                      'max_length': 'لطفا بیشتر از تعداد 50 وارد نکنید'
                                  },

                                  widget=forms.TextInput(attrs={
                                      'class': 'form-control',
                                      'placeholder': 'شماره تماس'

                                  }))
    age = forms.CharField(label='سن',
                          max_length=50,
                          error_messages={
                              'required': 'لطفا سن را وارد نمایید',
                              'max_length': 'لطفا بیشتر از تعداد 50 وارد نکنید'
                          },
                          widget=forms.TextInput(attrs={
                              'class': 'form-control',
                              'placeholder': 'سن'

                          }))
    address = forms.CharField(label='آدرس',
                              max_length=50,
                              error_messages={
                                  'required': 'لطفا آدرس را وارد نمایید',
                                  'max_length': 'لطفا بیشتر از تعداد 50 وارد نکنید'
                              },
                              widget=forms.TextInput(attrs={
                                  'class': 'form-control',
                                  'placeholder': 'آدرس'

                              }))
    information = forms.CharField(label='سوابق بیماری',
                                  max_length=50,
                                  error_messages={
                                      'required': 'لطفا سوابق بیماری را وارد نمایید',
                                      'max_length': 'لطفا بیشتر از تعداد 50 وارد نکنید'
                                  },
                                  widget=forms.TextInput(attrs={
                                      'class': 'form-control',
                                      'placeholder': 'سوابق بیماری'

                                  }))

    gender = forms.ChoiceField(label='جنسیت',
                               error_messages={
                                   'required': 'لطفا جنسیت را وارد نمایید',
                               },
                               widget=forms.Select(attrs={
                                   'class': 'form-select',
                               }))
