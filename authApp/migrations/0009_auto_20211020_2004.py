# Generated by Django 3.2.8 on 2021-10-21 01:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0008_alter_product_id_prod'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='check',
            name='date_fac',
        ),
        migrations.RemoveField(
            model_name='check',
            name='dni_cli',
        ),
        migrations.RemoveField(
            model_name='check',
            name='id_prod_fac',
        ),
        migrations.RemoveField(
            model_name='check',
            name='price_fac',
        ),
        migrations.RemoveField(
            model_name='check',
            name='user_fac',
        ),
    ]