from django import forms
from .models import ContactUS


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUS
        fields = ('name', 'email', 'phone', 'message')