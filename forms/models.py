from django.db import models


class FormTemplateField(models.Model):
    title = models.CharField(max_length=256)
    type = models.CharField(max_length=256)
    value = models.CharField(max_length=512)

    def __str__(self):
        return self.title

class FormTemplate(models.Model):
    name = models.CharField(max_length=256, blank=True)
    description = models.TextField(max_length=1024, blank=True)
    file = models.FileField(upload_to='uploads/form_templates/')

    fields = models.ManyToManyField(FormTemplateField, blank=True)

    def __str__(self):
        return self.name

class Form(models.Model):
    template = models.ForeignKey(
        FormTemplate,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=256)
    file = models.FileField(upload_to='uploads/forms/', blank=True)


