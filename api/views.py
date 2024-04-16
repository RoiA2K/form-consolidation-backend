from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import viewsets
from rest_framework.generics import RetrieveDestroyAPIView

from authentication.models import User
from authentication.serializer import UserSerializer, UserAuthSerializer
from forms.models import FormTemplate, Form, FormTemplateField
from forms.serializer import FormTemplateSerializer, FormSerializer, FormFieldSerializer

from PyPDF2 import PdfReader


# Create your views here.
class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FormsViewSet(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer

class FormFieldsViewSet(viewsets.ModelViewSet):
    queryset = FormTemplateField.objects.all()
    serializer_class = FormFieldSerializer

class FormTemplateView(APIView):
    serializer_class = FormTemplateSerializer
    
    def get(self, request):
        formTemplates = FormTemplate.objects.all()
        serializer = self.serializer_class(formTemplates, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        reader = PdfReader(instance.file.path)

        fields = reader.get_fields()
        for field_name, field_value in fields.items():
            form_field = FormTemplateField.objects.create(
                title=field_name,
                type='text',  # Assuming all fields are text type, you may need to adjust this based on your PDF
                value=field_value
            )
            instance.fields.add(form_field)
            # pass
        # print(fields.get('sample_title', {}).get('/V', None)) // Getting the field value


        return Response(serializer.data)


class FormTemplateDetailView(RetrieveDestroyAPIView):
    queryset = FormTemplate.objects.all()
    serializer_class = FormTemplateSerializer


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
        
