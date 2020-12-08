from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Recipe, Cookbook
from .forms import RecipeForm, CookbookForm
import pdfkit
from django.contrib.auth.decorators import login_required
from django.template import loader
import io



# Create your views here.

def index(request):
    recipes = Recipe.objects.all()
    search_name = request.GET.get('search_name')
    if search_name != '' and search_name is not None:
        recipes = recipes.filter(name__icontains=search_name)
    return render(request, 'recipeApp/index.html', {'recipes': recipes})


@login_required()
def create_cookbook(request):
    form = CookbookForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('recipeApp:library')

    return render(request, 'recipeApp/cookbook-form.html', {'form': form})


@login_required()
def library(request):
    books = Cookbook.objects.all()
    return render(request, 'recipeApp/library.html', {'books': books})


@login_required()
def delete_cookbook(request, id):
    book = Cookbook.objects.get(id=id)

    if request.method == 'POST':
        book.delete()
        return redirect('recipeApp:library')

    return render(request, 'recipeApp/cookbook-delete.html', {'book': book})


@login_required()
def cookbook(request, id):
    cookbook = Cookbook.objects.get(id=id)
    recipes = Recipe.objects.all()
    return render(request, 'recipeApp/cookbook.html', {'cookbook': cookbook, 'recipes': recipes})


@login_required()
def add_recipe(request):
    form = RecipeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('recipeApp:library')

    return render(request, 'recipeApp/recipe-form.html', {'form': form})


@login_required()
def update_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    form = RecipeForm(request.POST or None, instance=recipe)

    if form.is_valid():
        form.save()
        return redirect('recipeApp:library')

    return render(request, 'recipeApp/recipe-form.html', {'form': form, 'recipe': recipe})


def recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    return render(request, 'recipeApp/recipe.html', {'recipe': recipe})


def recipe_pdf(request, id):
    recipe = Recipe.objects.get(pk=id)
    template = loader.get_template('recipeApp/recipe_pdf.html')
    html = template.render({'recipe': recipe})
    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8'
    }
    pdf = pdfkit.from_string(html, False, options)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename = 'recipe.pdf'

    return response


@login_required()
def delete_recipe(request, id):

    recipe = Recipe.objects.get(id=id)

    if request.method == 'POST':
        recipe.delete()
        return redirect('recipeApp:library')

    return render(request, 'recipeApp/recipe-delete.html', {'recipe': recipe})