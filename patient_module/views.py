from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView

from . import models
from .models import Patient
from .forms import  AddPatientModelForm
from django.views import View


# Create your views here.

class PatientView(TemplateView):
    template_name = 'patient_module/patient.html'

    def get_context_data(self, **kwargs):
        patients = models.Patient.objects.all()
        context = super(PatientView,self).get_context_data()
        context['patients'] = patients
        return context

class PatientDetailView(TemplateView):
    template_name = 'patient_module/patient_details.html'

    def get_context_data(self, **kwargs,):
        context = super(PatientDetailView, self).get_context_data()
        patient_code = kwargs['patient_code']
        patient = get_object_or_404(Patient, pk=patient_code)
        context['patient'] = patient
        return context

class PatientAddView(View):
    def get(self, request):
        patient_form = AddPatientModelForm()
        context = {
            'patient_form': patient_form
        }
        return render(request, 'patient_module/add_patient_page.html', context)

    def post(self, request):
        patient_form = AddPatientModelForm(request.POST,)
        if patient_form.is_valid():
            patient_form.save()
            return redirect('patients')
        return render(request, 'patient_module/add_patient_page.html', {'patient_form': patient_form})

