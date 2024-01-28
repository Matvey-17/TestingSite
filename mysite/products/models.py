from django.db import models


class Product(models.Model):
    name_product = models.CharField(max_length=256, unique=True)
    count_used = models.IntegerField(default=0)

    def __str__(self):
        return self.name_product


class Recipe(models.Model):
    name_recipe = models.CharField(max_length=256, unique=True)
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
        return f'{self.recipe.name_recipe} | {self.product.name_product} {self.weight}г'
