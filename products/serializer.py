from rest_framework import serializers

from products.models import Product
from category.models import Category


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "title")


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "slug", 'category']


class ProductCreateSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(required=False)


class ProductSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(required=False)

    class Meta:
        model = Product
        fields = ["id", "title", "slug", 'category']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['category'] = ProductCategorySerializer(instance.category).data
        return data
