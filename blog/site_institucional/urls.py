from django.urls import path
from .views.home import HomeView
from .views.about import AboutPageView
from .views.contact import ContactView, AdminContactMessageListView, AdminContactDeleteView, AdminContactDetailView
from .views.article import ArticleListView, ArticleDetailView, AdminArticleCreateView, AdminArticleListView, AdminArticleUpdateView, AdminArticleDeleteView
from .views.login import AdminLoginView, AdminLogoutView
from .views.dashboard import DashboardView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('artigo/<slug:slug>/', ArticleDetailView.as_view(), name='article_detail'),
    path('artigos/', ArticleListView.as_view(), name='articles'),
    path('sobre_nos/', AboutPageView.as_view(), name='about'),
    path('contato/', ContactView.as_view(), name='contact'),
    path('control/', AdminLoginView.as_view(), name='admin_login'),
    path('control/dashboard/', DashboardView.as_view(), name='admin_dashboard'),
    path('control/articles/', AdminArticleListView.as_view(), name='admin_articles'),
    path('control/articles/<str:is_new>/', AdminArticleListView.as_view(), name='admin_articles_filtered'),
    path('control/article/create/<str:is_new>/', AdminArticleCreateView.as_view(), name='admin_article_create'),
    path('control/article/<int:pk>/edit/<str:is_new>/', AdminArticleUpdateView.as_view(), name='admin_article_edit'),
    path('control/article/delete/<int:id>/', AdminArticleDeleteView.as_view(), name='delete_article'),
    path('control/contacts/', AdminContactMessageListView.as_view(), name='admin_contact_list'),
    path('control/contacts/detail/<int:id>/', AdminContactDetailView.as_view(), name='admin_contact_detail'),
    path('control/contacts/delete/<int:id>/', AdminContactDeleteView.as_view(), name='admin_contact_delete'),
    path('control/logout/', AdminLogoutView.as_view(), name='logout'),
]