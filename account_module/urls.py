from django.urls import path
from . import views
urlpatterns = [
    path('',views.LoginView.as_view() ,name='login-page'),
    path('logout/', views.LogoutView.as_view(), name='logout-page'),

    path('register/', views.RegisterView.as_view(), name='register-page'),

    path('checkotp/',views.CheckOTPView.as_view(),name='check_otp'),
]