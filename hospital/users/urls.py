from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.views.decorators.cache import cache_page

from users.views import ProfileView, SignupView

app_name = 'users'

urlpatterns = [
    path('login/', cache_page(60)(LoginView.as_view(template_name='users/login.html')), name='login'),
    path('logout/', cache_page(60)(LogoutView.as_view(template_name='users/logout.html')), name='logout'),
    path('signup/', cache_page(60)(SignupView.as_view()), name='signup'),
    path('profile/', cache_page(60)(ProfileView.as_view()), name='profile'),
]