from django.urls import path
from . import views
urlpatterns = [
    path('',views.UserPanelView.as_view(),name='user_panel'),
    path('edit-profile/',views.EditProfileView.as_view(),name='edit_user_profile'),
]