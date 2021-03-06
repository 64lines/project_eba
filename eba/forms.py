from django import forms
from django.utils.translation import ugettext as _ 

class LoginForm(forms.Form):
    username = forms.CharField(label=_("Username"), required=True)
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput, required=True)
