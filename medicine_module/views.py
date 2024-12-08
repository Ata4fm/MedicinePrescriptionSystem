from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .forms import MedicineModelForm, SearchForm
from .models import Medicine

from rest_framework import viewsets, filters, permissions
from .serializers import MedicineSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50


class MedicineViewSet(viewsets.ModelViewSet):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser or not request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    serializer_class = MedicineSerializer
    queryset = Medicine.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["category"]
    search_fields = ["name"]
    pagination_class = StandardResultsSetPagination
    permission_classes = [permissions.IsAuthenticated,permissions.IsAdminUser]




@method_decorator(login_required, name='dispatch')
class MedicineView(ListView):
    model = Medicine
    template_name = 'medicine_module/medicine.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchForm
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser or not request.user.is_staff:
            return redirect(reverse('home'))
        return super().dispatch(request, *args, **kwargs)


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

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser or not request.user.is_staff:
            return redirect(reverse('home'))
        return super().dispatch(request, *args, **kwargs)