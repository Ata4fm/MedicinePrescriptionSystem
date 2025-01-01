"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

import rest_framework
from rest_framework.routers import DefaultRouter
from medicine_module.views import MedicineViewSet
from patient_module.views import PatientViewSet
from prescription_module.views import PrescriptionViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account_module.urls')),
    path('dashboard/patients/',include('patient_module.urls')),
    path('dashboard/',include('home.urls')),
    path('dashboard/medicine/',include('medicine_module.urls')),
    path('dashboard/medicine/prescription/',include('prescription_module.urls')),
    path('dashboard/user-panel/',include('user_panel_module.urls')),

    path("api-drf/", include("rest_framework.urls")),


]

router = DefaultRouter()
router.register("api/patients", PatientViewSet, basename="patients")
router.register("api/medicines", MedicineViewSet, basename="medicines")
router.register("api/prescription", PrescriptionViewSet, basename="prescription")
urlpatterns+= router.urls

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)