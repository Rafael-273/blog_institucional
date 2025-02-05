from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


# @method_decorator(login_required(login_url='/control'), name='dispatch')
class DashboardView(TemplateView):
    template_name = 'admin/dashboard.html'

    def dispatch(self, *args, **kwargs):
        print(self.request.user.is_authenticated)
        return super().dispatch(*args, **kwargs)