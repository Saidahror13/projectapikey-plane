from category.views import CategoryDetailView, CategoryListView
from django.urls import path

urlpatterns = [
    path('', CategoryListView.as_view(), name='category-list-create'),
    path('<int:pk>', CategoryDetailView.as_view(), name='category-detail'),
]

