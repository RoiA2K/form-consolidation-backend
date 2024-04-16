from rest_framework import serializers

from forms.models import FormTemplate, Form, FormTemplateField


class FormTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormTemplate
        fields = '__all__'

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = '__all__'

class FormFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormTemplateField
        fields = '__all__'

