from rest_framework import  serializers
from authApp.models import account
from authApp.models.account import Account
from authApp.models.user import User
from authApp.serializers.accountSerializer import AccountSerializer

class UserSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = User
        fields = ['is_superuser','id','username','password', 'name', 'email']

    def create(self,validated_data):
        
        user_instance = User.objects.create(**validated_data)

        return user_instance
    

    def to_representation(self, obj):
        user = User.objects.get(id = obj.id)
        
        return {
            'id': user.id,
            'username': user.username,
            'name': user.name,
            'email': user.email
        }