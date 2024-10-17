from django.urls import path

from accounts.views import RegisterView, UserLoginView, UserLogoutView, HomePageView

app_name = 'accounts'

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('', RegisterView.as_view(), name='register'),
]