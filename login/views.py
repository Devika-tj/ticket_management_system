from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import PENLoginForm


class PENLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = PENLoginForm
    redirect_authenticated_user = True


@login_required
def role_redirect(request):

    user = request.user

    if user.is_superuser or user.role == 'ADMIN':
        return redirect('admin_dashboard')

    elif user.role == 'SUPPORT':
        return redirect('support_dashboard')

    elif user.role == 'STAFF':
        return redirect('staff_dashboard')

    return render(
        request,
        'accounts/access_denied.html',
        status=403
    )


@login_required
def staff_dashboard(request):
    if request.user.role != 'STAFF':
        return redirect('role_redirect')

    return render(
        request,
        'accounts/staff_dashboard.html'
    )


@login_required
def support_dashboard(request):
    if request.user.role != 'SUPPORT':
        return redirect('role_redirect')

    return render(
        request,
        'accounts/support_dashboard.html'
    )


@login_required
def admin_dashboard(request):
    if not (
        request.user.is_superuser
        or request.user.role == 'ADMIN'
    ):
        return redirect('role_redirect')

    return render(
        request,
        'accounts/admin_dashboard.html'
    )


