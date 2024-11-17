from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import MedicineModelForm
from .models import Medicine

@method_decorator(login_required, name='dispatch')
class MedicineView(TemplateView):
    template_name = 'medicine_module/medicine.html'

    def get_context_data(self, **kwargs):
        medicine = Medicine.objects.all()
        context = super(MedicineView, self).get_context_data()
        context['medicines'] = medicine
        return context

@method_decorator(login_required, name='dispatch')
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