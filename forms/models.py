from django.db import models


class Form(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(max_length=1024, default='')
    file = models.FileField(upload_to='uploads/forms/', blank=True)
    