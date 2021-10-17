# Generated by Django 3.2.8 on 2021-10-17 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0003_rename_factura_check'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacturaProdRelacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factura_fac_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='factura', to='authApp.check')),
                ('prodcuto_pro_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='producto', to='authApp.product')),
            ],
        ),
    ]
