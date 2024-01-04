from django.contrib import admin
from .models import CategoryList, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {"slug": ("name",)}
    # autocomplete_fields = ['title']


@admin.register(CategoryList)
class CategoryListAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'category']
    prepopulated_fields = {"slug": ("name",)}
    # autocomplete_fields = ['title']
