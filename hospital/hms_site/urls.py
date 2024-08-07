from django.urls import path

from hms_site import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home')
]