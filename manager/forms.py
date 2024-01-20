from django import forms
from brand.models import ContactUS


class ReservationEditForm(forms.ModelForm):

    class Meta:
        model = ContactUS
        fields = ('name',)