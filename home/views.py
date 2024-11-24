
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView

from datetime import datetime
from jalali_date import date2jalali


@method_decorator(login_required,name='dispatch')
class HomeView(TemplateView):
    template_name = 'home/index.html'


def site_header_partial(request):
    dt = date2jalali(datetime.now()).strftime('%Y/%m/%d %A')
    context = {
        'datetime':dt,
    }
    return render(request,'shared/header_partial.html',context)