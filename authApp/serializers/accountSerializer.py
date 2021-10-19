from rest_framework import  serializers
from authApp.models import account
from authApp.models.account import Account
from authApp.models.check import Check
from authApp.models import check
from authApp.serializers.accountSerializer import AccountSerializer

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = fields = ['id','user','isActive']

    def create(self,validated_data):
      
        account = Account.objects.create(**validated_data)

        return account
    
    def to_representation(self, id):
        account_instance = Account.objects.get(id = id)

        return {
            'id': account_instance.id,
            'user': account_instance.user,
            'isActive': account_instance.isActive
           
            }