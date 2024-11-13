from django.urls import path
from . import views
urlpatterns = [
    path('',views.LoginView.as_view() ,name='login-page'),
    path('checkotp/',views.CheckOTPView.as_view(),name='check_otp'),
]