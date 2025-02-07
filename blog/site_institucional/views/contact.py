from django.views.generic import TemplateView, ListView, DeleteView, DetailView
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from ..forms.contact import ContactForm
from ..views.email_management import EmailManagementView
from ..models.contact import ContactMessage


class ContactView(TemplateView):
    template_name = 'front/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)

        if form.is_valid():
            contact_message = form.save()

            # subject = f"Nova mensagem de {contact_message.name} - {contact_message.subject}"
            # context = {
            #     'name': contact_message.name,
            #     'email': contact_message.email,
            #     'phone': contact_message.phone,
            #     'subject': contact_message.subject,
            #     'message': contact_message.message
            # }

            # template_name = 'email/contact_email.html'
            # to_emails = ['contatopinestudio@gmail.com']
            # email_sent = EmailManagementView.send_email(subject, template_name, context, to_emails)

            # if email_sent:
            #     messages.success(request, 'Mensagem enviada com sucesso!')
            #     return redirect('contact')

            # else:
            #     messages.error(request, 'Falha ao enviar o e-mail.')
            #     return redirect('contact')

        return JsonResponse({'status': 'error', 'message': 'Dados inválidos.'}, status=400)


class AdminContactMessageListView(ListView):
    model = ContactMessage
    template_name = 'admin/contact_list.html'
    context_object_name = 'contacts'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AdminContactDetailView(DetailView):
    model = ContactMessage
    template_name = "admin/contact_detail.html"
    context_object_name = "contact"

    def get_object(self, queryset=None):
        id = self.kwargs.get("id")
        return get_object_or_404(ContactMessage, id=id)
    

class AdminContactDeleteView(DeleteView):
    model = ContactMessage
    success_url = reverse_lazy('admin_contacts')

    def get_object(self, queryset=None):
        id = self.kwargs.get("id")
        return get_object_or_404(ContactMessage, id=id)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        messages.success(request, "Mensagem de contato deletada com sucesso!")
        return HttpResponseRedirect(self.success_url)

    def dispatch(self, request, *args, **kwargs):
        if request.method == "POST":
            return self.delete(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)