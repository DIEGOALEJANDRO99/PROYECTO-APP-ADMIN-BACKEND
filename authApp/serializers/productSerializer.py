from rest_framework import  serializers
from authApp.models import product
from authApp.models.product import Product
from authApp.serializers.accountSerializer import AccountSerializer


class ProductSerializer(serializers.ModelSerializer):


    class Meta:
        model = Product
        fields = fields = ['id_prod','name_prod','desc_prod', 'amount_prod','price_prod','size_prod']

    def create(self,validated_data):
      
        product = Product.objects.create(**validated_data)

        return product
    

    def to_representation(self, id_prod):
        product_instance = Product.objects.get(id_prod = id_prod)

        return {
            'id_prod': product_instance.id_prod,
            'name_prod': product_instance.name_prod,
            'desc_prod': product_instance.desc_prod,
            'amount_prod': product_instance.amount_prod,
            'price_prod': product_instance.price_prod,
            'size_prod' : product_instance.size_prod
                
            }
        