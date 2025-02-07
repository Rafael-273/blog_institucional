from django import forms
from ..models.contact import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 rounded-lg focus:outline-none focus:border-indigo-500 bg-[var(--secondary-color-dark)]'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-4 py-2 rounded-lg focus:outline-none focus:border-indigo-500 bg-[var(--secondary-color-dark)]'}),
            'phone': forms.TextInput(attrs={'class': 'w-full px-4 py-2 rounded-lg focus:outline-none focus:border-indigo-500 bg-[var(--secondary-color-dark)]'}),
            'subject': forms.TextInput(attrs={'class': 'w-full px-4 py-2 rounded-lg focus:outline-none focus:border-indigo-500 bg-[var(--secondary-color-dark)]'}),
            'message': forms.Textarea(attrs={'class': 'w-full px-4 py-2 rounded-lg focus:outline-none focus:border-indigo-500 bg-[var(--secondary-color-dark)]', 'rows': 4}),
        }