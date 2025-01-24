from PIL import Image
from django.db import models
from django.utils.text import slugify
from ._base import BaseModel


class Article(BaseModel):
    title = models.CharField(max_length=200, verbose_name="Title")
    subtitle = models.CharField(max_length=200, verbose_name="Subtitle")
    slug = models.SlugField(unique=True, blank=True, max_length=200)
    content = models.TextField(verbose_name="Content")
    cover = models.ImageField(upload_to='article_covers/', verbose_name="Cover Image")
    cover_caption = models.CharField(max_length=200, blank=True, null=True, verbose_name="Cover Caption")
    author = models.CharField(max_length=100)
    published = models.BooleanField(default=False, verbose_name="Published")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

        if self.cover:
            img = Image.open(self.cover.path)
            if img.height > 1200 or img.width > 1200:
                output_size = (1200, 1200)
                img.thumbnail(output_size)
                img.save(self.cover.path)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['-created_at']
