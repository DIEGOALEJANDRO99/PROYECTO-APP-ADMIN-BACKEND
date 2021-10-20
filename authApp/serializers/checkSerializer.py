
from rest_framework import  serializers
from authApp.models.check import Check
from authApp.models.user import User
from authApp.models.product import Product
from authApp.models import check
from authApp.serializers.accountSerializer import AccountSerializer

class CheckSerializer(serializers.ModelSerializer):

    class Meta:
        model = Check
        fields = fields = ['id_fac','dni_cli','user_fac','date_fac','id_prod_fac','price_fac']

    def create(self,validated_data):
        user = validated_data.pop('user_fac')
        product = validated_data.pop('id_prod_fac')
        check = Check.objects.create(**validated_data)
        user = User.objects.create(check_data = check, **user)
        product = Product.objects.create(check_data = check,**product)


        return check
    

    def to_representation(self, id_fac):
        check_instance = Check.objects.get(id_fac = id_fac)
        product_instance = Product.objects.get(id_prod = id_fac.id_prod)
        user_instance = User.objects.get(id=id_fac.id)

        return {
            'id_fac': check_instance.id_fac,
            'dni_cli': check_instance.dni_cli,
            'user_fac': user_instance.user_fac,
            'date_fac': check_instance.date_fac,
            'id_prod_fac': product_instance.id_prod,
            'price_fac' : check_instance.price_fac
            }