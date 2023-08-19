from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.SignupView.as_view(), name='signup'),
    path('update_profile', views.UpdateProfileView.as_view(), name='update_profile')
]