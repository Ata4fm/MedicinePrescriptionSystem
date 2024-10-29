from django.shortcuts import render
from .models import Medicine

# Create your views here.

def medicines(request):
    medicines = Medicine.objects.all()
    context = {
        'medicines': medicines
    }
    return render(request,'medicine_module/medicine.html',context)