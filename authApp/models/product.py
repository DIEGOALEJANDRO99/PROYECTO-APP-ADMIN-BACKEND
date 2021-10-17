from django.db import models


class Product(models.Model):
    
    id_prod = models.AutoField('Id',primary_key=True)
    name_prod = models.CharField('Prod_Name', max_length=100)
    desc_prod = models.DateField('Description')
    amount_prod = models.IntegerField('Amount_Product')
    price_prod = models.BigIntegerField('Price')
    size_prod = models.CharField('Size',max_length=1)