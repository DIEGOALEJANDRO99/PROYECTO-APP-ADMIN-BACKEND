from rest_framework import  serializers
from authApp.models.account import Account
from authApp.models.user import User
from authApp.serializers.accountSerializer import AccountSerializer

class UserSerializer(serializers.ModelSerializer):

    account  = AccountSerializer()

    class Meta:
        model = User
        fields = ['id','username','password', 'name', 'email','account']

    def create(self,validated_data):
        account_data = validated_data.pop('account')
        user_instance = User.objects.create(**validated_data)
        Account.objects.create(user = user_instance, **account_data)

        return user_instance

    

    