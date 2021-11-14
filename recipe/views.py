from django.views.generic import(ListView, CreateView, DetailView, UpdateView, DeleteView)

from .models import Recipe

from django.urls import reverse, reverse_lazy

class RecipeListView(ListView):
  model = Recipe

class RecipeCreateView(CreateView):
  model = Recipe
  fields = ["title", "content", "description"]
  success_url = reverse_lazy("recipe:index")

class RecipeDetailView(DetailView):
  model = Recipe

class RecipeUpdateView(UpdateView):
  model = Recipe
  fields = ["title", "content", "description"]
  success_url = "/"

class RecipeDeleteView(DeleteView):
  model = Recipe
  success_url = reverse_lazy("recipe:index")

def get_success_url(self):
  pk = self.kwargs.get("pk")
  return reverse("recipe:detail", kwargs={"pk":pk})