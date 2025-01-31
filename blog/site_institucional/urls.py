from django.urls import path
from .views.home import HomeView
from .views.about import AboutPageView
from .views.contact import ContactView
from .views.article import ArticleListView, ArticleDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('artigo/<slug:slug>/', ArticleDetailView.as_view(), name='article_detail'),
    path('artigos/', ArticleListView.as_view(), name='articles'),
    path('sobre_nos/', AboutPageView.as_view(), name='about'),
    path('contato/', ContactView.as_view(), name='contact'),
]