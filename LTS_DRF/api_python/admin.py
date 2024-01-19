from django.contrib import admin
from .models import PythonModel


@admin.register(PythonModel)
class Admin(admin.ModelAdmin):
    list_display = ['id', 'slug', 'title', 'content']
    prepopulated_fields = {"slug": ("title",)}
    # autocomplete_fields = ['title']


# @admin.register(CategoryList)
# class CategoryListAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'slug', 'category']
#     prepopulated_fields = {"slug": ("name",)}
#     # autocomplete_fields = ['title']
