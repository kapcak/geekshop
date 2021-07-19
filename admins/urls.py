from django.urls import path
from admins.views import admin_users, admin_users_create, admin_users_update, admin_users_remove, index, admin_product_read, admin_product_update, admin_product_remove

app_name = 'admins'
urlpatterns = [
    path('', index, name='index'),
    path('users/', admin_users, name='admin_users'),
    path('users/create/', admin_users_create, name='admin_users_create'),
    path('users/update/<int:pk>/', admin_users_update, name='admin_users_update'),
    path('users/remove/<int:pk>/', admin_users_remove, name='admin_users_remove'),
    path('products/', admin_product_read, name='admin_product_read'),
    path('products/update/<int:pk>/', admin_product_update, name='admin_product_update'),
    path('products/remove/<int:pk>/', admin_product_remove, name='admin_product_remove'),
]
