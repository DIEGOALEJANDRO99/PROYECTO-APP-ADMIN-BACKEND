from django.db import models
from .product import Product
from .user import User


class Check(models.Model):
    
    id_fac= models.AutoField('Id',primary_key=True)
    user_fac = models.ForeignKey(User, related_name='factura', on_delete=models.CASCADE)
    date_fac = models.DateField('Date')
    id_prod_fac = models.ForeignKey(Product ,related_name = 'product',on_delete=models.CASCADE)
    price_fac = models.BigIntegerField('Price') 