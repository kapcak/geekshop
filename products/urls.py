from django.urls import path
from products.views import  ProductListView, ProductCategoryView

app_name = 'products'
urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('category/<int:category_id>/', ProductCategoryView.as_view(), name='product'),
]