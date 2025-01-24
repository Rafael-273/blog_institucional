from django.views.generic import ListView
from ..models.article import Article


class HomeView(ListView):
    model = Article
    template_name = 'front/home.html'
    context_object_name = 'creatives'
    queryset = Article.objects.filter(published=True).order_by('-created_at')[:10]
