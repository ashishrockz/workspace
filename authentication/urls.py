from django.urls import path
from . import views


urlpatterns = [
    path('login', views.login, name='login'),  # Example URL pattern
    path('signup', views.signup, name='signup'),
]
