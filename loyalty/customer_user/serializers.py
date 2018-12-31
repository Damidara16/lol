from rest_framework import serializers
from django.contrib.auth.models import User
#from store_user.serializers import StoreSerializer
"""
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    #store = StoreSerializer()
    class Meta:
        model = Customer
        fields = ('user', 'uuid', 'birthdate', 'phone_number', 'gender', 'active', 'tier', 'total_spent', 'points')
"""
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    api_key = serializers.CharField()
"""
class RewardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reward
        fields = '__all__'

class DealSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reward
        fields = '__all__'

class TransactionSerialers(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = '__all__'
"""
