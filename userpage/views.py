from django.views.generic import TemplateView

from recipe.models import Recipe

class UserpageTemplateView(TemplateView):
  template_name = "userpage/index.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    if self.request.user.is_authenticated:
      context['recipe_list'] = Recipe.objects.filter(user=self.request.user)
    else:
      context['recipe_list'] = None

    return context