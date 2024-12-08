from django.urls import path
from . import views

urlpatterns = [
    path('', views.PrescriptionView.as_view(), name='prescription'),
    path('add-prescription', views.add_medicine_to_prescription, name='add-prescription-to-prescription'),
    path('remove-prescription-detailremove-prescription-detail',views.remove_prescription_basket_detail,name='remove-prescription-basket-detail'),
    path('change-prescription-detail-count',views.change_order_detail_count,name='change-prescription-detail-count'),
]