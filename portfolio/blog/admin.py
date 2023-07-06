from django.contrib import admin
from .models import Timestamp, MetaData, Tag, Category, Post


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('created_at', 'updated_at')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('created_at', 'updated_at')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('status', 'created_at', 'updated_at')
    filter_horizontal = ('category', 'tag')
