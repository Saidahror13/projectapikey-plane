from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from products.models import Product
from products.serializer import ProductListSerializer


@api_view(["GET"])
def get_products_list(request):
    products = Product.objects.order_by("-id")
    # products_data = [{"id": product.id, "title": product.title} for product in products]
    serializer = ProductListSerializer(products, many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# def get_product(request, slug):
#     product = get_object_or_404(Product, slug=slug)
#     serializer = ProductListSerializer(product)
#     return Response(serializer.data)
#
# #
# @api_view(['GET','POST'])




