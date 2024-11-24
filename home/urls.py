from django.urls import path
from . import views

urlpatterns = [

    path('',views.HomeView.as_view(),name='home'),
    path('site-header', views.site_header_partial, name='site_header_partial'),

]