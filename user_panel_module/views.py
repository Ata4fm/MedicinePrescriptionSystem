from django.http import HttpRequest, JsonResponse, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic import TemplateView, View

from patient_module.models import Patient
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
