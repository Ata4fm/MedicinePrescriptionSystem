from django.urls import path
from . import views

urlpatterns = [
    path('' , views.PatientView.as_view(), name='patients'),
    path('/patient_information/<int:patient_code>', views.PatientDetailView.as_view(), name='patient_information'),
    path('/add_patient/', views.PatientAddView.as_view(), name='add_patient'),

]