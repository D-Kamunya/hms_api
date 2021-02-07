from rest_framework import  serializers
from django.db import models
from .models import CustomUser as User,Doctor,Patient
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework.exceptions import AuthenticationFailed



# User serializer
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name', 'last_name','role','address','mobile', 'email') 


# Doctor serializer
class DocSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True, many=False)
    class Meta:
        model = Doctor
        fields = '__all__'


# Patient serializer
class PatientSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True, many=False)
    class Meta:
        model = Patient
        fields = '__all__'




# Register serializer
class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','role','first_name', 'last_name','address','mobile','password')
        extra_kwargs = {
            'password':{'write_only': True},
        }
    def create(self, validated_data):
      user = User.objects.create_user(**validated_data)
      return user


# Login serializer
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    role = serializers.CharField(read_only=True)
    is_verified = serializers.BooleanField(read_only=True)

    def validate(self, data):
        email = data['email']
        password = data['password']
        user = authenticate(email=email, password=password)

        if user is None:
            raise AuthenticationFailed("Invalid login credentials")
        if not user.is_verified:
            raise AuthenticationFailed('Email Not Verified')    

        try:
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)

            update_last_login(None, user)

            validation = {
                'access': access_token,
                'refresh': refresh_token,
                'email': user.email,
                'role': user.role,
            }

            return validation
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid login credentials")      