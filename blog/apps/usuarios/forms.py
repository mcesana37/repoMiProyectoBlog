from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django.contrib.auth import authenticate, login


class RegistroForm(UserCreationForm):
    email = forms.EmailField(label='Correo', required=True)
    first_name = forms.CharField(label='Nombre', required=True)
    last_name = forms.CharField(label='Apellido', required=True)
    password1 = forms.CharField(
        label='Contraseña', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(
        label='Confirmar Contraseña', widget=forms.PasswordInput, required=True)

    class Meta:
        model = Usuario
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        ]

class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(label='Contraseña, widget=forms.PasswordImput')

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)

