from django import forms

from prescription_module.models import Prescription


class PatientForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['patient']
        widgets = {
            'patient': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'بیمار',
                }
            ),
        }


