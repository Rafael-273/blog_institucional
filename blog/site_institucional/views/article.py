from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
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
        is_news = self.kwargs.get('is_new')
        queryset = Article.objects.all()

        if is_news in ['true', 'false']:
            queryset = queryset.filter(is_news=is_news == 'true')

        if query:
            queryset = queryset.filter(Q(title__icontains=query) | Q(subtitle__icontains=query))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        context['selected_category'] = self.request.GET.get('category', '')
        context['is_new'] = self.kwargs.get('is_new', None) 
        return context


class AdminArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'admin/article_list.html'
    context_object_name = 'articles'
    paginate_by = 10
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('admin_login')
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        is_new = self.kwargs.get('is_new', None)

        if is_new is not None:
            if is_new.lower() == 'true':
                self.is_new_filter = True
                return Article.objects.filter(is_news=True)
            elif is_new.lower() == 'false':
                self.is_new_filter = False
                return Article.objects.filter(is_news=False)
        self.is_new_filter = None
        return Article.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_new_filter'] = self.is_new_filter

        return context


class AdminArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'admin/create/article_create.html'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('admin_login')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        is_new = self.kwargs.get('is_new', 'false')
        
        if is_new.lower() == 'true':
            form.instance.is_news = True
        else:
            form.instance.is_news = False
        
        article = form.save(commit=False)
        article.save()
        return redirect(reverse('admin_articles_filtered', kwargs={'is_new': is_new}))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        is_new = self.kwargs.get('is_new', 'false')
        is_new_filter = True if is_new.lower() == 'true' else False
        context['is_new_filter'] = is_new_filter
        return context


class AdminArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'admin/edit/article_edit.html'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('admin_login')
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        is_new = self.kwargs.get('is_new', 'false')
        is_new_filter = True if is_new.lower() == 'true' else False
        context['is_new_filter'] = is_new_filter
        article = self.object

        context.update({
            'article': article,
        })
        return context

    def form_valid(self, form):
        is_new = self.kwargs.get('is_new', 'false')
        article = form.save(commit=False)
        article.save()
        return redirect(reverse('admin_articles_filtered', kwargs={'is_new': is_new}))


class AdminArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('admin_articles')
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('admin_login')
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        id = self.kwargs.get("id")
        return get_object_or_404(Article, id=id)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        messages.success(request, "Artigo deletado com sucesso!")
        return HttpResponseRedirect(self.success_url)

    def dispatch(self, request, *args, **kwargs):
        if request.method == "POST":
            return self.delete(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)