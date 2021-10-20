from rest_framework import  serializers
from authApp.models import account
from authApp.models.account import Account
from authApp.models.user import User
from authApp.models.check import Check
from authApp.models import check


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = fields = ['id','user','isActive']

    def create(self,validated_data):
      
        user = User.validated_data.pop('user')
        account = Account.objects.create(**validated_data)
        User.objects.create(account_data = account,**user)
        return account
    
    def to_representation(self, id):
        account_instance = Account.objects.get(id = id)
        user_instance = User.objects.get(id=id)

        return {
            'id': account_instance.id,
            'user': user_instance.user,
            'isActive': account_instance.isActive
    
            }