from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=125)
    price = serializers.DecimalField(decimal_places=2, max_digits=100000000) 

    def create(self, validated_data):
        product_instance = Product(**validated_data)
        return product_instance