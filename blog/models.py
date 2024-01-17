from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    slug = models.CharField(max_length=100, null=True, blank=True, verbose_name='slug')
    text = models.TextField(null=True, blank=True, verbose_name='содержимое')
    preview = models.ImageField(upload_to='blogs/', null=True, blank=True, verbose_name='изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создано')
    published = models.BooleanField(default=True, verbose_name='опубликовано')
    views = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return f'Статья: {self.title} '

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
        ordering = ['-id']
