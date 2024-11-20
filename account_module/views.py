from django.http import HttpRequest
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from django.contrib.auth.models import User
from .forms import LoginForm,CheckOTPForm,RegisterForm
from .models import OTP
from patient_module.models import Patient
import random

import ghasedakpack

sms = ghasedakpack.Ghasedak('0f5ca0462d55e9ed8c1118b234c3bf78b19a21b7f91b5703d3b2480cde975cb0')




class LoginView(View):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


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
            otpcode = random.randint(100000,999999)
            user: User = Patient.objects.filter(code__iexact=user_code).first()
            print(user.phonenumber)
            if user is not None:
                OTP.objects.create(phone=user.phonenumber, code=otpcode)
                sms.verification({'receptor': user.phonenumber,
                                  'type': '1',
                                  'template': 'randcode',
                                  'param1': otpcode})
                request.session['phonenumber'] = user.phonenumber
                return redirect(reverse('check_otp'))
            else:
                login_form.add_error('code','اطلاعات کد ملی اشتباه است')
        context = {
            'form': login_form
        }
        return render(request, 'account_module/login.html', context)


class CheckOTPView(View):
    def get(self, request):
        form = CheckOTPForm()
        context = {
            'form': form
        }
        return render(request, 'account_module/otpcheck.html',context)

    def post(self, request):
        phone_number = request.session['phonenumber']
        otp_form = CheckOTPForm(request.POST)
        if otp_form.is_valid():
            user_code = otp_form.cleaned_data.get('otp')
            user: User = Patient.objects.filter(phonenumber__iexact=phone_number).first()
            if OTP.objects.filter(code= user_code, phone=phone_number).exists():
                login(request, user)
                OTP.objects.filter(code= user_code, phone=phone_number).delete()
                return redirect(reverse('home'))
            else:
                otp_form.add_error('otp','کد وارد شده اشتباه میباشد')
        else:
            otp_form.add_error("otp","فرم معتبر نیست")
        context = {
            'form': otp_form
        }
        return render(request, 'account_module/otpcheck.html',context)

class RegisterView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register.html', context)
    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_username = register_form.cleaned_data.get('username')
            user_code = register_form.cleaned_data.get('code')
            user_phone = register_form.cleaned_data.get('phonenumber')
            user : bool = Patient.objects.filter(code__iexact=user_code).exists()
            if user:
                register_form.add_error('code', 'این بیمار با این کد ملی وجود دارد')
            else:
                new_user = Patient(username=user_username,code=user_code,phonenumber=user_phone)
                new_user.save()
                return redirect(reverse('login-page'))
        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register.html', context)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login-page'))