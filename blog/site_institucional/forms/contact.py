from django import forms
from ..models.contact import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 rounded-lg focus:outline-none focus:border-indigo-500 bg-[var(--secondary-color-dark)] text-white'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-4 py-2 rounded-lg focus:outline-none focus:border-indigo-500 bg-[var(--secondary-color-dark)] text-white'}),
            'phone': forms.TextInput(attrs={'class': 'w-full px-4 py-2 rounded-lg focus:outline-none focus:border-indigo-500 bg-[var(--secondary-color-dark)] text-white'}),
            'subject': forms.TextInput(attrs={'class': 'w-full px-4 py-2 rounded-lg focus:outline-none focus:border-indigo-500 bg-[var(--secondary-color-dark)] text-white'}),
            'message': forms.Textarea(attrs={'class': 'w-full px-4 py-2 rounded-lg focus:outline-none focus:border-indigo-500 bg-[var(--secondary-color-dark)] text-white', 'rows': 4}),
        }