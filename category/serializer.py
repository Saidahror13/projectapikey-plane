from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from category.models import Category
from products.models import Product


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'position', 'parent']


class CategoryCreateSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(required=False)

    class Meta:
        model = Category
        fields = ['id', 'title', 'position', 'parent']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['category'] = ProductCategorySerializer(instance.category).data
        return data


