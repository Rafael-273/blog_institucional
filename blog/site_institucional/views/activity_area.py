from django.views.generic import TemplateView


class ExecucaoPenaView(TemplateView):
    template_name = "front/areas/execucao_pena.html"


class PrevidenciarioView(TemplateView):
    template_name = "front/areas/previdenciario.html"


class CriminalView(TemplateView):
    template_name = "front/areas/criminal.html"


class FamiliarView(TemplateView):
    template_name = "front/areas/familiar.html"


class CivelView(TemplateView):
    template_name = "front/areas/civel.html"
