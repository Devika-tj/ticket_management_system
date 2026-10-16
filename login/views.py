from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView
)
from django.shortcuts import render
from django.urls import reverse_lazy 
from .forms import LoginForm


class UserLoginView(LoginView):

    template_name = 'login/login.html'

    authentication_form = LoginForm

    redirect_authenticated_user = True


    def get_success_url(self):

        role = self.request.user.role


        if role == 'support':

            return '/support/dashboard/'


        if role == 'admin':
            return '/admin-panel/dashboard/'
        
        return '/tickets/'
    
    class UserPasswordChangeView(PasswordChangeView): 
        template_name = 'login/change_password.html'
        success_url = reverse_lazy('login')

class UserLogoutView(LogoutView):

    next_page = '/login/'