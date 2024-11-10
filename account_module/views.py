from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from .forms import LoginForm
from patient_module.models import Patient


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'form': login_form
            }
        return render(request, 'account_module/login.html', context)

    def post(self, request: HttpRequest):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_code = login_form.cleaned_data.get('code')
            user: User = Patient.objects.filter(code__iexact=user_code).first()
            if user is not None:
                login(request, user)
                return redirect(reverse('home'))
            else:
                login_form.add_error('code','اطلاعات کد ملی اشتباه است')
        context = {
            'form': login_form
        }
        return render(request, 'account_module/login.html', context)