

from django.http import HttpRequest, JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import TemplateView, View, ListView, DetailView

from patient_module.models import Patient
from prescription_module.models import Prescription
from .forms import EditProfileModelForm




class UserPanelView(TemplateView):
    template_name = 'user_panel_module/user_panel_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class EditProfileView(View):
    def get(self, request:HttpRequest):
        current_user = Patient.objects.filter(pk=request.user.code).first()
        edit_form = EditProfileModelForm(instance=current_user)
        context = {'form': edit_form}
        return render(request, 'user_panel_module/edit_profile_component.html', context)

    def post(self, request:HttpRequest):
        current_user = Patient.objects.filter(pk=request.user.code).first()
        edit_form = EditProfileModelForm(request.POST,request.FILES,instance=current_user)
        if edit_form.is_valid():
            edit_form.save(commit=True)
            return JsonResponse({'success': True})  # اگر فرم موفق بود
        html = render_to_string('user_panel_module/edit_profile_component.html',
                                {'form': edit_form}, request)
        return JsonResponse({'success': False, 'html': html})


class MyPrescription(ListView):
    model = Prescription
    template_name = 'user_panel_module/my_my-prescription.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        request: HttpRequest = self.request
        queryset = queryset.filter(patient_id=request.user.code, is_submitted=True)
        return queryset

class MyPrescriptionDetail(DetailView):
    template_name = 'user_panel_module/my_my-prescription-detail.html'
    model = Prescription

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse('login'))
        return super().dispatch(request, *args, **kwargs)