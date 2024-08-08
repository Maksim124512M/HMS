from django.urls import path

from hms_site import views

app_name = 'hms_site'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home')
]