from django.shortcuts import render
from django.views.generic import TemplateView, FormView

from patient_module.forms import AddPatientModelForm


# Create your views here.

class LoginView(FormView):
    template_name = 'account_module/login.html'
    form_class = AddPatientModelForm
    success_url = '/patients/'