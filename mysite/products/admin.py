from django.contrib import admin

from mysite.products.models import Product, Recipe, RecipeProduct


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name_product', 'count_used']


class RecipeProductInline(admin.TabularInline):
    model = RecipeProduct
    extra = 0


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeProductInline]
    list_display = ['name_recipe', 'products']
