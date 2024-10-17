from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from accounts.forms import RegisterForm, LoginForm


class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('accounts:login')

class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = LoginForm
    success_url = reverse_lazy('accounts:home')

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('accounts:home')

class HomePageView(TemplateView):
    template_name = 'home.html'
