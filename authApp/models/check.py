from django.db import models
from .product import Product
from .user import User


class Check(models.Model):
    
    id_fac= models.AutoField('Id',primary_key=True)
    dni_cli = models.BigIntegerField('dni_cli', default=0)
    user_fac = models.ForeignKey(User, related_name='factura', on_delete=models.CASCADE,default=None)
    date_fac = models.DateTimeField('Date',default=None)
    id_prod_fac= models.ForeignKey(Product ,related_name = 'product',on_delete=models.CASCADE, default=None)
    price_fac = models.BigIntegerField('Price',default=None) 