from django.urls import path
from admins.views import UserCreateView, UserListView, UserUpdateView, UserDeleteView, index, admin_product_read, admin_product_update, admin_product_remove, admin_product_create

app_name = 'admins'
urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users/create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='admin_users_update'),
    path('users/remove/<int:pk>/', UserDeleteView.as_view(), name='admin_users_remove'),
    path('products/', admin_product_read, name='admin_product_read'),
    path('products/update/<int:pk>/', admin_product_update, name='admin_product_update'),
    path('products/remove/<int:pk>/', admin_product_remove, name='admin_product_remove'),
    path('products/create/', admin_product_create, name='admin_product_create'),
]
