from django.contrib import admin
from django.urls import path

from lib.views import IndexTemplateView
from recipe.views import RecipeListView, RecipeCreateView, RecipeDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipe/', RecipeListView.as_view(), name="recipe-index"),
    path('recipe/create', RecipeCreateView.as_view(), name="recipe-create"),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name="recipe-detail"),
    path('', IndexTemplateView.as_view(), name="index"),
]
