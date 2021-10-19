
from rest_framework import  serializers
from authApp.models.check import Check
from authApp.models import check
from authApp.serializers.accountSerializer import AccountSerializer

class CheckSerializer(serializers.ModelSerializer):

    class Meta:
        model = Check
        fields = fields = ['id_fac','dni_cli','user_fac','date_fac','id_prod_fac','price_fac']

    def create(self,validated_data):
      
        check = Check.objects.create(**validated_data)

        return check
    

    def to_representation(self, id_fac):
        check_instance = Check.objects.get(id_fac = id_fac)

        return {
            'id_fac': check_instance.id_fac,
            'dni_cli': check_instance.dni_cli,
            'user_fac': check_instance.user_fac,
            'date_fac': check_instance.date_fac,
            'id_prod_fac': check_instance.id_prod_fac,
            'price_fac' : check_instance.price_fac
            }