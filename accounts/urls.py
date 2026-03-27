from django.urls import path
from accounts.views import Registerview, LoginView,ProfileView

urlpatterns = [
    path('register/',Registerview.as_view(),name='register'),
    path('login/',LoginView.as_view(), name='login'),
    path('profile/',ProfileView.as_view(),name='profile')
]


