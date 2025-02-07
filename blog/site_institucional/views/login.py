from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from ..forms.login import AuthenticationForm


class AdminLoginView(LoginView):
    authentication_form = AuthenticationForm
    template_name = 'admin/login.html'

    def get_success_url(self):
        return reverse('admin_dashboard')
    
    def form_invalid(self, form):
        messages.error(self.request, "Usuário ou senha incorretos. Tente novamente.")
        return super().form_invalid(form) 


class AdminLogoutView(LogoutView):
    next_page = reverse_lazy('admin_login')

