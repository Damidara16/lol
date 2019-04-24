from rest_framework import serializers
from content.models import *
from .models import *


class OptionsSelectSerializer(serializers.Serializer):
    applied = serializers.BooleanField(default=False)
    name = serializers.CharField()
    selected = serializers.CharField()

class OptionsNumSerializer(serializers.Serializer):
    applied = serializers.BooleanField(default=False)
    name = serializers.CharField()
    amount = serializers.IntegerField()


class OptionsSerializer(serializers.Serializer):
    noption = OptionsNumSerializer(many=True)
    soption = OptionsSelectSerializer(many=True)

class CartItemSerializer(serializers.Serializer):
    name = serializers.CharField()
    amount = serializers.IntegerField()
    option = OptionsSerializer()

class CartMetaSerializer(serializers.Serializer):
    price = serializers.IntegerField()
    mop = serializers.CharField()
    orderNum = serializers.CharField()
    transaction_id = serializers.CharField()

class CartSerializer(serializers.Serializer):
    item = CartItemSerializer()
    metadata = CartMetaSerializer()


class InvItemSerializer(serializers.Serializer):
    pass

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('name', 'abbr', 'item_serial_id', 'active_inventory', 'picture', 'categories')


class ProductsSerializer(serializers.ModelSerializer):
    items = ItemSerializer(source='item_set', many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('store', 'name', 'number_of_items', 'items')
