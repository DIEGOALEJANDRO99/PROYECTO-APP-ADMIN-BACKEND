# Generated by Django 3.2.8 on 2021-10-21 01:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0010_check_dni_cli'),
    ]

    operations = [
        migrations.AddField(
            model_name='check',
            name='user_fac',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='factura', to=settings.AUTH_USER_MODEL),
        ),
    ]