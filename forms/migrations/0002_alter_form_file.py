# Generated by Django 5.0.4 on 2024-04-11 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='file',
            field=models.FileField(blank=True, upload_to='uploads/forms/'),
        ),
    ]