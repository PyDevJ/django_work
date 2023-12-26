from django.urls import path
from main.views import index, contact, product, add_product
from main.apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contact', contact, name='contact'),
    path('add_product', add_product, name='add_product'),
    path('product/<int:product_id>', product, name='product')
]
