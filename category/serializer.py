from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from category.models import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'title', 'position', 'parent']
