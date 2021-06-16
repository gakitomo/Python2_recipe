from django.shortcuts import render

from .models import Recipe

class RecipeListView(ListView):
  model = Recipe