from django import forms
from django.forms import ModelForm

from medicine_module.models import Medicine


class MedicineModelForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name', 'short_desc', 'category']

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'نام دارو',
                }
            ),
            'short_desc': forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder': 'دستور مصرف'
                }
            ),

        }