from django.urls import path

from products.views import ProductDetailView, ProductListView

urlpatterns = [
    path("", ProductListView.as_view(), name="products-list"),
    path("<int:pk>", ProductDetailView.as_view(), name="products-detail"),

]
