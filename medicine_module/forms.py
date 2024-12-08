from django import forms
from django.forms import ModelForm
from django.core import validators

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

class SearchForm(forms.Form):
    search = forms.CharField(
        label='جستجو',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control shadow-sm',
                'v-model':'search',
                'placeholder': 'جستجو',
            }
        ),

    )