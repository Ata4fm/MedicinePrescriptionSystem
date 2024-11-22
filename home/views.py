from datetime import datetime
from jalali_date import date2jalali
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView



@method_decorator(login_required,name='dispatch')
class HomeView(TemplateView):
    template_name = 'home/index.html'


    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data()
        context['datetime'] = date2jalali(datetime.now()).strftime('%Y/%m/%d %A')
        return context
