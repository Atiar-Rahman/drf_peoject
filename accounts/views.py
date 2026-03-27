from rest_framework import generics
from accounts.models import User
from accounts.serializers import RegisterSerializer

class Registerview(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class =  RegisterSerializer