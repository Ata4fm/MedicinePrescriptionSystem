from django.urls import path
from . import views
from .views import PatientSearchAPIView

urlpatterns = [
    path('', views.PrescriptionView.as_view(), name='prescription'),
    path('submit-prescription/', views.verify_prescription, name='submit-prescription'),
    path('add-prescription/', views.add_medicine_to_prescription, name='add-prescription-to-prescription'),
    path('remove-prescription-detail/',views.remove_prescription_basket_detail,name='remove-prescription-basket-detail'),
    path('change-prescription-detail-count/',views.change_order_detail_count,name='change-prescription-detail-count'),
    path('api/patient-search/', PatientSearchAPIView.as_view(), name='patient-search'),
]