from . import views
from django.urls import path

app_name = 'recipeApp'
urlpatterns = [
    path('', views.index, name="index"),
    path('create-cookbook/', views.create_cookbook, name="create-cookbook"),
    path('library/', views.library, name="library"),
    path('add-recipe/', views.add_recipe, name="add-recipe"),
    path('recipe/', views.recipe, name="recipe"),
    path('cookbook/<int:id>', views.cookbook, name="cookbook"),
    path('recipe/<int:id>', views.recipe, name="recipe"),
    path('update/<int:id>', views.update_recipe, name="update_recipe"),
    path('delete-cookbook/<int:id>', views.delete_cookbook, name="delete_cookbook"),
    path('delete-recipe/<int:id>', views.delete_recipe, name="delete_recipe"),
    path('<int:id>/', views.recipe_pdf, name="recipe_pdf"),
]
