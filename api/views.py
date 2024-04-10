from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from authentication.models import User
from authentication.serializer import UserSerializer
from forms.models import Form
from forms.serializer import FormSerializer


# Create your views here.
class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FormsViewSet(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
