from rest_framework import serializers

from store.models import Product


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'image', 'price', 'token']