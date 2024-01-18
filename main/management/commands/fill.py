from django.core.management import BaseCommand
from main.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        """ Удаление базы данных и наполнение данными """
        Category.objects.all().delete()
        Product.objects.all().delete()

        # заполнение категорий
        category_list = [{
            "pk": 1,
            "name": "овощи",
            "description": "Продукты питания"
            },
            {
                "pk": 2,
                "name": "фрукты",
                "description": "Всё фруктовое разнообразие"
            },
            {
                "pk": 3,
                "name": "электроника",
                "description": "Цифровая и бытовая техника"
            },
            {
                "pk": 4,
                "name": "напитки",
                "description": "Натуральные соки, газировки, компоты"
            }, ]

        categories = []
        for category in category_list:
            categories.append(Category(**category))

        Category.objects.bulk_create(categories)

        product_list = [{
            "pk": 1,
            "name": "часы",
            "description": "с электронным табло и радио",
            "category": categories[2],
            "price": "99.99",
        },
            {
                "pk": 2,
                "name": "картофель",
                "description": "грунтовая",
                "category": categories[0],
                "price": "30.00",
            },
            {
                "pk": 3,
                "name": "картофель",
                "description": "парниковая",
                "category": categories[0],
                "price": "28.50",
            },
            {
                "pk": 4,
                "name": "яблоко",
                "description": "летние сорта",
                "preview": "products/apple.jpg",
                "category": categories[1],
                "price": "120.00",
            },
            {
                "pk": 5,
                "name": "кола",
                "description": "без сахара",
                "category": categories[3],
                "price": "120.99",
            },
            {
                "pk": 6,
                "name": "кола Pus",
                "description": "с сахаром",
                "category": categories[3],
                "price": "150.49",
            },
            {
                "pk": 7,
                "name": "лемонад",
                "description": "напиток сильногазированный",
                "category": categories[3],
                "price": "70.00",
            },
            {
                "pk": 8,
                "name": "смарт-часы",
                "description": "наручные умные часы",
                "category": categories[2],
                "price": "4000",
            }, ]

        products = []
        for product in product_list:
            products.append(Product(**product))

        Product.objects.bulk_create(products)
