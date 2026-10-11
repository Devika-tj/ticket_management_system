from django.contrib.auth.views import (
    LoginView,
    LogoutView
)

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

<<<<<<< HEAD
            return '/admin-panel/dashboard/'
=======
    return render(
        request,
        'accounts/support_staff_dashboard.html'
    )
>>>>>>> 82df279bf52b0f355fac946df2c5d9634d173ff1


        return '/tickets/'


class UserLogoutView(LogoutView):

    next_page = '/login/'