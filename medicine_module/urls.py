from django.urls import path
from . import views

urlpatterns = [
    path("", views.medicines, name="medicines"),
    path("/add_medicine",views.AddMedicine.as_view(),name="add_medicine"),
]