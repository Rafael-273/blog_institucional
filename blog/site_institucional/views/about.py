from django.views.generic import TemplateView


class AboutPageView(TemplateView):
    template_name = 'front/about.html'
