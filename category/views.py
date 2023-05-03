from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from category.serializer import CategorySerializer, Category


# Create your views here.


class CategoryListView(APIView):
    def get(self, request):
        queryset = Category.objects.order_by('-id')
        serial = CategorySerializer(queryset, many=True)
        return Response(serial.data)

    def post(self, request):
        serial = CategorySerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_200_OK)
        return Response(serial.data, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Category, pk=pk)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        serial = CategorySerializer(self.get_object(pk))
        return Response(serial.data)

    def put(self, request, category_serializer=CategorySerializer, *args, **kwargs):
        pk = kwargs.get('pk')
        serializer = category_serializer(instance=self.get_object(pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        serial = self.get_object(pk)
        serial.delete()
        return Response(status=status.HTTP_400_BAD_REQUEST)

