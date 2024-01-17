from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from main.forms import ProductForm
from main.models import Product, Contact


class ProductListView(ListView):
    model = Product
    template_name = 'main/index.html'
    paginate_by = 4


class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    # fields = ('name', 'description', 'preview', 'category', 'price',)
    success_url = reverse_lazy('main:index')
    # template_name = 'main/product_form.html'


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('main:index')


class ContactListView(ListView):
    model = Contact
    template_name = 'main/contact.html'


class ContactCreateView(CreateView):
    model = Contact
    fields = ('name', 'email',)
    success_url = reverse_lazy('main:contact')
    # template_name = 'main/contact_form.html'
