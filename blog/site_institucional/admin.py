from django.contrib import admin
from .models import article, contact

admin.site.register(article.Article)
admin.site.register(contact.ContactMessage)