from django.urls import path
from . import views

urlpatterns = [
    path('' , views.patient_view, name='patients'),
    path('/patient_information/<int:patient_code>', views.patient_view_detail, name='patient_information'),
    path('/add_patient/', views.patient_add_view, name='add_patient'),

]