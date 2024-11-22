from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path("", views.MedicineView.as_view(), name="medicines"),
    path("add_medicine",views.AddMedicine.as_view(),name="add_medicine"),
]

router = DefaultRouter()
router.register("api/medicines", views.MedicineViewSet, basename="medicines")
urlpatterns+= router.urls