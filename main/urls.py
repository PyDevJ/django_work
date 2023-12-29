from django.urls import path
from main.views import ProductListView, ProductDetailView, ProductCreateView, ContactListView, ContactCreateView
from main.apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contact/', ContactListView.as_view(), name='contact'),
    path('contact_form/', ContactCreateView.as_view(), name='contact_form'),
    path('add_product/', ProductCreateView.as_view(), name='add_product'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product')
]
