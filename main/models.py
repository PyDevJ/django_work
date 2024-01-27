import psycopg2
from django.conf import settings
from django.db import models, connection
from django.db.models.signals import post_save
from django.dispatch import receiver

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField()

    def __str__(self):
        return f'Категория: {self.id} Наименование: {self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='products/', verbose_name='изображение', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.DecimalField(decimal_places=2, max_digits=16, verbose_name='цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    changed_at = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')
    owner_product = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='владелец')
    is_published = models.BooleanField(default=False, verbose_name="публикация")

    def __str__(self):
        return f'Продукт: {self.id} {self.name} по цене {self.price} в категории {self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['-id']

        permissions = [
            ('set_description',
             'редактирование описания продукта'),
            ('set_category',
             'редактирование категории продукта'),
            ('set_is_published',
             'редактирование статуса публикации продукта'),
        ]


class Contact(models.Model):
    name = models.CharField(max_length=20, verbose_name='имя')
    email = models.EmailField(max_length=254, verbose_name='почта')

    def __str__(self):
        return f'Имя: {self.name} Email: {self.email}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    name = models.CharField(max_length=150, verbose_name='Название версии')
    number = models.FloatField(verbose_name='Номер версии')
    is_active = models.BooleanField(default=False, verbose_name='Активна')

    @classmethod
    def truncate_table_restart_id(cls):
        """Метод для обнуления счетчика автоинкремента"""

        with connection.cursor() as cur:
            try:
                cur.execute(f'TRUNCATE TABLE {cls._meta.db_table} RESTART IDENTITY CASCADE')
            except psycopg2.errors.Error as e:
                raise e

    def __str__(self):
        return f'{self.name} {self.number}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'


@receiver(post_save, sender=Version)
def set_active_version(sender, instance, **kwargs):
    """При установке флага версии в режим 'активна' версии, которые были активны до этого перестают быть активными"""
    if instance.is_active:
        Version.objects.filter(product=instance.product).exclude(pk=instance.pk).update(is_active=False)
