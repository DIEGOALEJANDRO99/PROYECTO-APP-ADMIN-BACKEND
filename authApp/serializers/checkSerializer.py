
from rest_framework import  serializers
from authApp.models.check import Check
from authApp.models.user import User
from authApp.models.product import Product
from authApp.models import check
from authApp.serializers.accountSerializer import AccountSerializer

class CheckSerializer(serializers.ModelSerializer):

    class Meta:
        model = Check
        fields ='__all__'

   