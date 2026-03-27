from rest_framework import serializers
from accounts.models import User
from django.contrib.auth import authenticate

# register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password', 'role']
        extra_kwargs = {
            'password': {'write_only': True},
            'role': {'required': False}
        }

    def create(self, validated_data):
        validated_data['role'] = 'user'  # force user role
        return User.objects.create_user(**validated_data)



# login serializer
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self,data):
        user = authenticate(
            username = data['email'],
            password = data['password']
        )

        if not user:
            raise serializers.ValidationError("Invalid credentials")
        

        data['user'] = user
        return data
    
