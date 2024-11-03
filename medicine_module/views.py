from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import MedicineModelForm
from .models import Medicine
from django.views import View
# Create your views here.

class MedicineView(TemplateView):
    template_name = 'medicine_module/medicine.html'

    def get_context_data(self, **kwargs):
        medicine = Medicine.objects.all()
        context = super(MedicineView, self).get_context_data()
        context['medicines'] = medicine
        return context


class AddMedicine(View):
    def get(self,request):
        medicine_form = MedicineModelForm()
        context = {
            'medicine_form': medicine_form
        }
        return render(request,'medicine_module/add_medicine.html',context)


    def post(self,request):
        medicine_form = MedicineModelForm(request.POST)
        if medicine_form.is_valid():
            medicine_form.save()
            return redirect('medicines')

        return render(request,'medicine_module/add_medicine.html',{
            'medicine_form': medicine_form
        })