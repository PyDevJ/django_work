from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.core.cache import cache
from django.forms import inlineformset_factory
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from main.models import Product, Contact, Version, Category
from main.forms import ProductForm, VersionForm, ContactForm
from main.services import get_categories_cache


class ProductListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Product
    permission_required = 'main.view_product'
    template_name = 'main/index.html'
    paginate_by = 5
    extra_context = {
        'title': 'Каталог продуктов'
    }

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', '-changed_at')
        return ordering


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    permission_required = 'main.view_product'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # низкоуровневое кеширование
        if settings.CACHE_ENABLED:
            key = f'subject_list_{self.object.pk}'
            subject_list = cache.get(key)
            if subject_list is None:
                subject_list = self.object.version_set.all()
                cache.set(key, subject_list)
        else:
            subject_list = self.object.version_set.all()

        context_data['subjects'] = subject_list
        return context_data


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    permission_required = 'main.add_product'
    success_url = reverse_lazy('main:index')

    def form_valid(self, form):
        # formset = self.get_context_data()['formset']
        self.object = form.save()
        self.object.owner_product = self.request.user
        self.object.save()
        # if formset.is_valid():
        #     formset.instance = self.object
        #     formset.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    permission_required = 'main.change_product'
    success_url = reverse_lazy('main:index')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)
        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

    def get_form(self, form_class=None):
        """
        Если у пользователя нет прав на редактирование поля, то удаляем его из формы.
        """
        form = super().get_form(form_class)
        if self.object.owner_product != self.request.user:
        # if self.request.user.has_perms(['main.change_product']):
            product_fields = [f for f in form.fields.keys()]
            for field in product_fields:
                if not self.request.user.has_perm(f'main.set_{field}'):
                    del form.fields[field]
        return form

    def test_func(self):
        """
        Если пользователь не владелец продукта или нет разрешения на изменение или не суперюзер,
        то не может его изменять.
        """
        # return (self.get_object().owner_product == self.request.user)

        obj = self.get_object()
        return (obj.owner_product == self.request.user
                or self.request.user.has_perms(['main.change_product'])
                or self.request.user.is_superuser)

    def handle_no_permission(self):
        raise Http404('У вас нет прав для изменения этого товара')


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('main:index')

    def test_func(self):
        return self.request.user.is_superuser


class ContactListView(ListView):
    model = Contact
    template_name = 'main/contact.html'


class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('main:contact')


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'main/categories.html'
    extra_context = {
        'title': 'Категории',
        'object_ist': get_categories_cache
    }

    def get_queryset(self):
        return get_categories_cache()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список категорий'
        return context
