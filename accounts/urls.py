from django.urls import path
from accounts.views import Registerview

urlpatterns = [
    path('register/',Registerview.as_view(),name='register')
]


