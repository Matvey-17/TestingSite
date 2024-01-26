from django.db import models


class Product(models.Model):
    name_product = models.CharField(max_length=256)
    count_used = models.IntegerField(default=0)

    def __str__(self):
        return self.name_product


class Recipe(models.Model):
    name_recipe = models.CharField(max_length=256)
    products = models.ManyToManyField(Product, through='RecipeProduct')

    def __str__(self):
        return self.name_recipe


class RecipeProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    weight = models.IntegerField()

    class Meta:
        unique_together = ('product', 'recipe')

    def __str__(self):
        return f'{self.product.name} | {self.recipe.name} | {self.weight}'
