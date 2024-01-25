from django.urls import path
from main.views import ProductListView, ProductDetailView, ProductCreateView, ContactListView, ContactCreateView, \
    ProductUpdateView, ProductDeleteView
from main.apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contact/', ContactListView.as_view(), name='contact'),
    path('contact_form/', ContactCreateView.as_view(), name='contact_form'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),
]
