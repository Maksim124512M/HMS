from django.urls import path

from appointments import views


app_name = 'appointments'

urlpatterns = [
    path('doctors/', views.OurDoctorsView.as_view(), name='our_doctors'),
    path('doctor/<int:pk>', views.DoctorDetailView.as_view(), name='doctor_detail'),
    path('feedback-update/<int:pk>', views.FeedbackUpdateView.as_view(), name='feedback_update'),
    path('feedback-delete/<int:pk>', views.FeedbackDeleteView.as_view(), name='feedback_delete'),
]