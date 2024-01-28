from django.shortcuts import render
from models import Recipe, Product, RecipeProduct
from django.db.models import F


def add_product_to_recipe(request):
    recipe_id = request.GET.get('recipe_id')
    product_id = request.GET.get('product_id')
    weight = request.GET.get('weight')

    recipe = Recipe.objects.get(id=recipe_id)
    product = Product.objects.get(id=product_id)

    get_recipe, is_create = RecipeProduct.objects.get_or_create(
        recipe=recipe,
        product=product,
        defaults={'weight': weight}
    )

    if not is_create:
        get_recipe.weight = weight
        get_recipe.save()


def cook_recipe(request):
    recipe_id = request.GET.get('recipe_id')
    recipe = Recipe.objects.get(id=recipe_id)

    for product in recipe.products.all():
        product.count_used = F('count_used') + 1
        product.save()
        product.refresh_from_db()


def show_recipes_without_product(request):
    product_id = request.GET.get('product_id')
    product = Product.objects.get(id=product_id)

    response = (Recipe.objects.exclude(recipeproduct__product=product) | Recipe.objects.filter(
        recipeproduct__product=product, recipeproduct__weight__lt=10))
    content = {'response': response}

    return render(request, 'show_recipes.html', content)
