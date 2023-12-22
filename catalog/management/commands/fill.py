from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        # print('Hi, Sky!')
        category_list = [
            {'name': 'обувь', 'description': 'вся обувь'},
            {'name': 'электроника', 'description': 'оргтехника'},
            {'name': 'косметика', 'description': 'духи, крема, салфетки'},
        ]

        # база заполняется построчно
        # for category_item in category_list:
        #     Category.objects.create(**category_item)

        category_for_create = []

        # предварительно зачищаeт все данные в таблице
        Category.objects.all().delete()

        for category_item in category_list:
            category_for_create.append(
                Category(**category_item)
            )

        # print(category_for_create)

        Category.objects.bulk_create(category_for_create)
