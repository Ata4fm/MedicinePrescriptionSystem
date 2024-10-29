from django.shortcuts import render, get_object_or_404, redirect
from . import models
from .models import Patient
from .forms import AddPatientForm


# Create your views here.

def patient_view(request):
    patients = models.Patient.objects.all()
    context = {'patients': patients}
    return render(request, 'patient_module/patient.html',context)

def patient_view_detail(request, patient_code):
    patient = get_object_or_404(Patient,pk=patient_code)
    context = {'patient': patient}
    return render(request,'patient_module/patient_details.html',context)

def patient_add_view(request):
    if request.method == 'POST':
        patient_form = AddPatientForm(request.POST,)
        if patient_form.is_valid():
            return redirect('home')
    else:
        patient_form = AddPatientForm()
    context = {
        'patient_form': patient_form
    }
    return render(request, 'patient_module/add_patient_page.html',context)