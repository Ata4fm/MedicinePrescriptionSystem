from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView
from django.views.generic.edit import FormView
from .models import Patient
from .forms import  AddPatientModelForm


from rest_framework import viewsets, filters
from .serializers import PatientSerializer
from django_filters.rest_framework import DjangoFilterBackend



class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.filter(is_superuser=False)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["gender"]
    search_fields = ["code"]


# Create your views here.
@method_decorator(login_required, name='dispatch')
class PatientView(ListView):
    template_name = 'patient_module/patient.html'
    model = Patient



    def get_queryset(self):
        base_query = super(PatientView, self).get_queryset()
        data = base_query.filter(is_superuser=False)
        return data



@method_decorator(login_required, name='dispatch')
class PatientDetailView(DetailView):
    template_name = 'patient_module/patient_details.html'
    model = Patient

@method_decorator(login_required, name='dispatch')
class PatientAddView(FormView):
    template_name = 'patient_module/add_patient_page.html'
    form_class = AddPatientModelForm
    success_url = '/patients'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

