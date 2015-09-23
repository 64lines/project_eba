from django import forms

USERNAME_LABEL = 'Nombre de usuario'
PASSWORD_LABEL = 'Clave'

class LoginForm(forms.Form):
    username = forms.CharField(label=USERNAME_LABEL, required=True)
    password = forms.CharField(label=PASSWORD_LABEL, widget=forms.PasswordInput, required=True)
