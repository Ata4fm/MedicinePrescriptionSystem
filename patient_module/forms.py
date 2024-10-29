from django import forms

class AddPatientForm(forms.Form):
    firstname = forms.CharField()
    lastname = forms.CharField()
    phonenumber = forms.CharField()
