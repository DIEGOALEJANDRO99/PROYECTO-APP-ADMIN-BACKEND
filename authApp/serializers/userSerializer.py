from rest_framework import  serializers
from authApp.models import account
from authApp.models.account import Account
from authApp.models.user import User
from authApp.serializers.accountSerializer import AccountSerializer

class UserSerializer(serializers.ModelSerializer):

    account  = AccountSerializer()

    class Meta:
        model = User
        fields = ['is_superuser','id','username','password', 'name', 'email','account']

    def create(self,validated_data):
        account_data = validated_data.pop('account')
        user_instance = User.objects.create(**validated_data)
        Account.objects.create(user = user_instance, **account_data)

        return user_instance
    

    def to_representation(self, obj):
        user = User.objects.get(id = obj.id)
        account = Account.objects.get(user=obj.id)

        return {
            'id': user.id,
            'username': user.username,
            'name': user.name,
            'email': user.email,
            'account':{
                'id': account.id,
                'balance': account.balance,
                'lastChangeDate': account.lastChangeDate,
                'isActive': account.isActive
            }
        }