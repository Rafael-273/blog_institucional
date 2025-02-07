from django import forms
from ..models.article import Article
from django.forms import inlineformset_factory
from django.utils.text import slugify


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'subtitle', 'author', 'cover', 'cover_caption', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg',
                'placeholder': 'Digite o título do artigo'
            }),
            'subtitle': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg',
                'placeholder': 'Digite o subtítulo do artigo'
            }),
            'cover_caption': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg',
                'placeholder': 'Digite a legenda da capa'
            }),
            'author': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg',
                'placeholder': 'Digite o nome do autor'
            }),
            'cover': forms.ClearableFileInput(attrs={
                'class': 'w-full px-4 py-2 border rounded-lg text-gray-700 bg-white transition duration-200'
            }),
            'content': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border rounded-lg text-gray-700 bg-white transition duration-200'
            }),            
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError("O título deve ter pelo menos 5 caracteres.")

        if Article.objects.filter(title=title).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Já existe um artigo com este título. Escolha um título diferente.")
        return title

    def save(self, commit=True):
        article = super().save(commit=False)

        if commit:
            article.save()
            self.save_m2m()

        return article