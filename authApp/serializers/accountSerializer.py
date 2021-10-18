from rest_framework import serializers
from authApp.models.account import Account

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['id','balance', 'lastChangeDate', 'isActive']