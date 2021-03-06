# Generated by Django 3.2.8 on 2021-10-17 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id_fac', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('date_fac', models.DateField(verbose_name='Date')),
                ('price_fac', models.BigIntegerField(verbose_name='Price')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id_prod', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('name_prod', models.CharField(max_length=100, verbose_name='Prod_Name')),
                ('desc_prod', models.DateField(verbose_name='Description')),
                ('amount_prod', models.IntegerField(verbose_name='Amount_Product')),
                ('price_prod', models.BigIntegerField(verbose_name='Price')),
                ('size_prod', models.CharField(max_length=1, verbose_name='Size')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='balance',
            field=models.BigIntegerField(default=500000, verbose_name='Balance'),
        ),
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.AddField(
            model_name='factura',
            name='id_prod_fac',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='authApp.product'),
        ),
        migrations.AddField(
            model_name='factura',
            name='user_fac',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='factura', to=settings.AUTH_USER_MODEL),
        ),
    ]
