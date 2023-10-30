# forms.py
from django import forms

class ConfirmationForm(forms.Form):
    confirm = forms.BooleanField(required=True, initial=True, widget=forms.HiddenInput)