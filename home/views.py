
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView

from datetime import datetime
from jalali_date import date2jalali

from medicine_module.models import Medicine
from patient_module.models import Patient
from prescription_module.models import Prescription


@method_decorator(login_required,name='dispatch')
class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doctors']= Patient.objects.filter(is_superuser=True).count()
        context['patients'] = Patient.objects.filter(is_superuser=False).count()
        context['medicines'] = Medicine.objects.all().count()
        context['prescriptions'] = Prescription.objects.filter(is_submitted=True).count()
        return context

def site_header_partial(request):
    dt = date2jalali(datetime.now()).strftime('%Y/%m/%d %A')
    context = {
        'datetime':dt,
    }
    return render(request,'shared/header_partial.html',context)