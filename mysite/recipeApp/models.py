from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Cookbook(models.Model):
    def __str__(self):

        return self.book_name

    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    book_name = models.CharField(max_length=200)
    book_description = models.TextField()


class Recipe(models.Model):
    def __str__(self):

        return self.name

    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=200)
    description = models.TextField()
    total_time = models.CharField(max_length=200)
    image = models.ImageField(default='recipe.jpg', upload_to='recipe_pics')
    ingredients = models.TextField()
    instructions = models.TextField()
    notes = models.TextField()








