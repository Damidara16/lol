from rest_framework import serializers
from .models import Store

class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = '__all__'

class LoginPosSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    #api_key = serializers.CharField()
