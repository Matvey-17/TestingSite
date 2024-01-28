from django.contrib import admin

from . import models


class RecipeProductInline(admin.TabularInline):
    model = models.RecipeProduct
    extra = 0


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [RecipeProductInline]
    list_display = ['name_product', 'count_used']


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeProductInline]
    list_display = ['name_recipe']


admin.site.register(models.RecipeProduct)
