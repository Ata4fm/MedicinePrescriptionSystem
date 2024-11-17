from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

@method_decorator(login_required,name='dispatch')
class HomeView(TemplateView):
    template_name = 'home/index.html'



# Create your views here.
