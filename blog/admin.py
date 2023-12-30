from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text')
    list_filter = ('title',)
    search_fields = ('title', 'text')
