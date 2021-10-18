from django.db import models
from authApp.models.check import Check
from authApp.models.product import Product


class CheckProduct(models.Model):
    factura_fac_id = models.ForeignKey(Check, related_name='factura', on_delete=models.CASCADE)
    prodcuto_pro_id = models.ForeignKey(Product, related_name='producto', on_delete=models.CASCADE)