from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views

urlpatterns = [
    path('' , views.PatientView.as_view(), name='patients'),
    path('patient_information/<int:pk>', views.PatientDetailView.as_view(), name='patient_information'),
    path('add_patient', views.PatientAddView.as_view(), name='add_patient'),

]
router = DefaultRouter()
router.register("api/patients", views.PatientViewSet, basename="patients")
urlpatterns+= router.urls