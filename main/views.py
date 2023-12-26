from django.shortcuts import render
from main.models import Product, Category, Contact
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.core.files.storage import FileSystemStorage


def index(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 4)
    page_number = request.GET.get("page")
    products = []
    page_obj = paginator.get_page(page_number)
    products.extend(page_obj)
    return render(request, 'main/index.html', context={'products': products, 'title': 'Главная', 'page_obj': page_obj})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        if name is not None and email is not None:
            contact = Contact.objects.filter(name=name)
            if not contact:
                Contact.objects.create(name=name, email=email)
            contacts = Contact.objects.all()
            return render(request, 'main/contact.html', context={'name': name, 'email': email, 'contacts': contacts, 'title': 'Контакты'})
    contacts = Contact.objects.all()
    return render(request, 'main/contact.html', context={'contacts': contacts, 'title': 'Контакты'})


def product(request, product_id: int):
    try:
        product = Product.objects.get(pk=product_id)
        product_info = {'product': product, 'title': 'Продукт'}
        return render(request, 'main/product.html', context=product_info)
    except ObjectDoesNotExist:
        product_info = {'product': Product.objects.get(pk=1), 'title': 'Продукт'}
        return render(request, 'main/product.html', context=product_info)


def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        if request.FILES:
            file = request.FILES['preview']
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
        else:
            filename = ''
        category_name = request.POST.get('category')
        price = request.POST.get('price')
        if name is not None :
            product = Product.objects.filter(name=name)
            if not product:
                category = Category.objects.filter(name=category_name)
                if category:
                    Product.objects.create(name=name, description=description, preview=filename, category=category[0], price=price)
                    return render(request, 'main/add_product.html', context={'success': True})
    return render(request, 'main/add_product.html')
