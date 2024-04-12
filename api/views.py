from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import viewsets

from authentication.models import User
from authentication.serializer import UserSerializer, UserAuthSerializer
from forms.models import Form
from forms.serializer import FormSerializer


# Create your views here.
class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FormsViewSet(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer

class UserLoginView(APIView):
    def post(self, request):
        pass

class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "registered"})

class UserLoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Wrong Password!')
        
        return Response({"message": "Logged in!"})
        

