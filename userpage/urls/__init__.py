from django.urls import path, include

from ..views import UserpageTemplateView 

app_name = "userpage"

urlpatterns = [
  path("", UserpageTemplateView.as_view(), name="index"),
  path("recipe/", include("userpage.urls.recipe", namespace="recipe")),
]