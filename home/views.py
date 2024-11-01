from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = 'home/index.html'


def prescribing_medication(request):
    return render(request,'prescribing_medication.html')
def patient_info(request):
    return render(request,'patient_info.html')

# Create your views here.
