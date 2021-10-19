from django.db import models
from django.db.models.manager import ManagerDescriptor


class Product(models.Model):
    
    id_prod = models.AutoField('Id',primary_key=True)
    name_prod = models.CharField('Prod_Name', max_length=100)
    desc_prod = models.CharField('Description', max_length=500)
    amount_prod = models.IntegerField('Amount_Product')
    price_prod = models.BigIntegerField('Price')
    size_prod = models.CharField('Size',max_length=1)

    def create_product(self,name_prod,desc_prod,amount_prod,price_prod,size_prod):
    
        if not name_prod:
            raise ValueError("Producto sin nombre")
        product = self.model(name_prod=name_prod)
        product.set_firstname(name_prod)
        product.save(using = self._db)

        return product

    
