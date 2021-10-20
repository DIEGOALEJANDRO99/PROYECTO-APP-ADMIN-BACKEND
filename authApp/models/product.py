from django.db import models
from django.db.models.manager import ManagerDescriptor
from rest_framework.status import HTTP_404_NOT_FOUND


class Product(models.Model):
    
    id_prod = models.IntegerField('Id',primary_key=True)
    name_prod = models.CharField('Prod_Name', max_length=100)
    desc_prod = models.CharField('Description', max_length=500)
    amount_prod = models.IntegerField('Amount_Product')
    price_prod = models.BigIntegerField('Price')
    size_prod = models.CharField('Size',max_length=1)

  
  
    
