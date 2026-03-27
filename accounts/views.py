from rest_framework import generics
from accounts.models import User
from accounts.serializers import RegisterSerializer,LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsAdminUserRole


class Registerview(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class =  RegisterSerializer


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)

        return Response(
            {
                'message':'Login successful',
                'access':str(refresh.access_token),
                'refresh':str(refresh),
                'user':{
                    'id':user.id,
                    'email':user.email,
                    'role':user.role
                }
            },status=status.HTTP_200_OK
        )
    
# profile view

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        return Response({
            'email':request.user.email,
            'role':request.user.role
        })
    

class AdminOnlyView(APIView):
    permission_classes = [IsAdminUserRole]

    def get(self,request):
        return Response({
            'message':'Welcome admin'
        })
    
    