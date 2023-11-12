from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'custom-input', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'custom-input', 'placeholder': 'Email adress'}),
            'subject': forms.TextInput(attrs={'class': 'custom-input', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'custom-textarea', 'placeholder': 'Your message'}),
        }

