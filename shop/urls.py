
from django.contrib import admin
from django.urls import path
from djangoProject4.views import index
from shop.views import create_customer, create_product, index_shop, update_price, add_to_basket, basket

urlpatterns = [
    path('', index_shop),
    path('create_customer/', create_customer, name = 'create_customer'),
    path('create_product/', create_product, name = 'create_product'),
    path('update_price/', update_price, name = 'update_price'),
    path('add_to_basket/', add_to_basket, name = 'add_to_basket'),
    path('basket/', basket, name = 'basket')
]
