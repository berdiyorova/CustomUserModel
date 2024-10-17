from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from accounts.models import UserModel


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('full_name', 'phone', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    email = forms.EmailField(required=True)
