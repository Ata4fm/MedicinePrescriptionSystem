
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from rest_framework.pagination import PageNumberPagination

from .forms import MedicineModelForm
from .models import Medicine

from rest_framework import viewsets, filters
from .serializers import MedicineSerializer
from django_filters.rest_framework import DjangoFilterBackend

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 1000

class MedicineViewSet(viewsets.ModelViewSet):
    serializer_class = MedicineSerializer
    queryset = Medicine.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["category"]
    search_fields = ["name"]
    pagination_class = StandardResultsSetPagination




@method_decorator(login_required, name='dispatch')
class MedicineView(ListView):
    model = Medicine
    template_name = 'medicine_module/medicine.html'
    paginate_by = 2


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