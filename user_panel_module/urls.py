from django.urls import path
from . import views
urlpatterns = [
    path('',views.UserPanelView.as_view(),name='user_panel'),
    path('my-prescription',views.MyPrescription.as_view(),name='my-prescription'),
    path('my-prescription/detail/<int:pk>', views.MyPrescriptionDetail.as_view(), name='my-prescription-detail'),
    path('edit-profile/',views.EditProfileView.as_view(),name='edit_user_profile'),
]