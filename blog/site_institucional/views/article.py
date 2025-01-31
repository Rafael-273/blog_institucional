from django.shortcuts import redirect
from django.forms import modelform_factory
from django.utils.text import slugify
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic import DetailView, ListView, DeleteView, UpdateView, View
from django.views.generic.edit import CreateView
from django.db.models import Q
from ..forms.article import ArticleForm
from ..models.article import Article
from django.contrib import messages


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'front/article.html'
    context_object_name = 'article'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)       
        return context


class ArticleListView(ListView):
    model = Article
    template_name = 'front/article_list.html'
    context_object_name = 'article_list'
    paginate_by = 9

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        category_slug = self.request.GET.get('category', '')
        queryset = Article.objects.all()

        if category_slug:
            queryset = queryset.filter(categories__slug=category_slug)

        if query:
            queryset = queryset.filter(Q(title__icontains=query) | Q(subtitle__icontains=query))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        context['selected_category'] = self.request.GET.get('category', '')
        return context
    

class AdminArticleListView(ListView):
    model = Article
    template_name = 'admin/article_list.html'
    context_object_name = 'articles'
    paginate_by = 10
    
    def get_queryset(self):
        return Article.objects.all()