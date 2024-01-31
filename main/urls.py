from django.urls import path
from django.views.decorators.cache import cache_page

from main.views import ProductListView, ProductDetailView, ProductCreateView, ContactListView, ContactCreateView, \
    ProductUpdateView, ProductDeleteView, CategoryListView
from main.apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contact/', ContactListView.as_view(), name='contact'),
    path('contact_form/', ContactCreateView.as_view(), name='contact_form'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('product/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),
    path('categories/', CategoryListView.as_view(), name='categories'),
]
