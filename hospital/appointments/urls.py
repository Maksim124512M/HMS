from django.urls import path
from django.views.decorators.cache import cache_page

from appointments import views


app_name = 'appointments'

urlpatterns = [
    path('doctors/', cache_page(60)(views.OurDoctorsView.as_view()), name='our_doctors'),
    path('doctor/<int:pk>', cache_page(60)(views.DoctorDetailView.as_view()), name='doctor_detail'),
    path('feedback-update/<int:pk>', cache_page(60)(views.FeedbackUpdateView.as_view()), name='feedback_update'),
    path('feedback-delete/<int:pk>', cache_page(60)(views.FeedbackDeleteView.as_view()), name='feedback_delete'),
]