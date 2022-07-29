from django import forms
from .models import *


class groupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']


class paymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['date', 'description', 'divide_type', 'payer']
