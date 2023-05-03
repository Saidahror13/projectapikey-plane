from django.urls import path

from products.views import ProductList, ProductDetailView

urlpatterns = [
    path("", ProductList.as_view(), name="products-list"),
    path("<int:pk>", ProductDetailView.as_view(), name="products-detail"),

]
