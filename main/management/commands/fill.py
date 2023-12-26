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
            "description": "Различные овощные культуры"
        },
            {
                "pk": 2,
                "name": "фрукты",
                "description": "Различные фрукты"
            },
            {
                "pk": 3,
                "name": "мясо",
                "description": "Мясные продукты"
            },
            {
                "pk": 4,
                "name": "напитки",
                "description": "Безалкогольные напитки"
            }, ]
        # for item in category_list:
        #     Category.objects.create(**item)
        categories = []
        for category in category_list:
            categories.append(Category(**category))

        Category.objects.bulk_create(categories)

        product_list = [{
            "pk": 1,
            "name": "морковь",
            "description": "морковь обыкновенная",
            "category": categories[0],
            "price": "30.99",
        },
            {
                "pk": 2,
                "name": "капуста белокочанная",
                "description": "капуста обыкновенная",
                "category": categories[0],
                "price": "60.00",
            },
            {
                "pk": 3,
                "name": "яблоки",
                "description": "яблоко Леголь",
                "category": categories[1],
                "price": "70.50",
            },
            {
                "pk": 4,
                "name": "бананы",
                "description": "бананы Гондурас",
                "category": categories[1],
                "price": "121.99",
            },
            {
                "pk": 5,
                "name": "свинина",
                "description": "свинина экстра",
                "category": categories[2],
                "price": "379.99",
            },
            {
                "pk": 6,
                "name": "куриное филе",
                "description": "куриное филе Приосколье",
                "category": categories[2],
                "price": "254.50",
            },
            {
                "pk": 7,
                "name": "сок гранатовый",
                "description": "сок гранатовый первого отжима",
                "category": categories[3],
                "price": "229.99",
            },
            {
                "pk": 8,
                "name": "нектар манго",
                "description": "нектар манго осветленный",
                "category": categories[3],
                "price": "119.99",
            },]
        products = []
        for product in product_list:
            products.append(Product(**product))

        Product.objects.bulk_create(products)
