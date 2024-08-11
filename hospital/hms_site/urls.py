from django.urls import path
from django.views.decorators.cache import cache_page

from hms_site import views

app_name = 'hms_site'

urlpatterns = [
    path('', cache_page(60)(views.HomeView.as_view()), name='home')
]