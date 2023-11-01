
from django.contrib import admin
from django.urls import path
from djangoProject4.views import index
from shop.views import create_customer, create_product

urlpatterns = [
    path('', index),
    path('create_customer/', create_customer, name = 'create_customer'),
    path('create_product/', create_product, name = 'create_product')
]
