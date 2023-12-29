from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
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
    fields = ('name', 'description', 'preview', 'category', 'price',)
    success_url = reverse_lazy('main:index')
    template_name = 'main/add_product.html'


class ContactListView(ListView):
    model = Contact
    template_name = 'main/contact.html'


class ContactCreateView(CreateView):
    model = Contact
    fields = ('name', 'email',)
    success_url = reverse_lazy('main:contact')
    template_name = 'main/contact_form.html'
