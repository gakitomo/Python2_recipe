from django.urls import path

from .views import UserpageTemplateView 

app_name = "userpage"

urlpatterns = [
  path("", UserpageTemplateView.as_view(), name="index"), 
]