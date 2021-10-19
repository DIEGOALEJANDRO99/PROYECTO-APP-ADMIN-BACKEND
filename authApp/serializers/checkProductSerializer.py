from rest_framework import  serializers
from authApp.models.check import Check
from authApp.models.checkProduct import CheckProduct
from authApp.models import checkProduct
from authApp.serializers.accountSerializer import AccountSerializer

class CheckProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = CheckProduct
        fields = fields = ['factura_fac_id','prodcuto_pro_id']

    def create(self,validated_data):
      
        checkProduct = CheckProduct.objects.create(**validated_data)

        return checkProduct


    def to_representation(self, factura_fac_id):
        checkProduct_instance = CheckProduct.objects.get(factura_fac_id = factura_fac_id)

        return {
            'factura_fac_id': checkProduct_instance.factura_fac_id,
            'prodcuto_pro_id': checkProduct_instance.prodcuto_pro_id
            }