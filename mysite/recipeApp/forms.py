from django import forms
from .models import Recipe, Cookbook

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'image', 'total_time', 'ingredients', 'instructions', 'notes']


class CookbookForm(forms.ModelForm):
    class Meta:
        model = Cookbook
        fields = ['book_name', 'book_description']


