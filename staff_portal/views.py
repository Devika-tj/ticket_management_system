<<<<<<< HEAD
from django.contrib import messages

from django.contrib.auth import (
    update_session_auth_hash
)

from django.contrib.auth.decorators import login_required

from django.shortcuts import (
    redirect,
    render
)

from .forms import (
    SupportHubPasswordChangeForm
)


@login_required
def profile(request):

    return render(
        request,
        'staff_portal/profile.html'
    )


@login_required
def change_password(request):

    if request.method == 'POST':

        form = SupportHubPasswordChangeForm(
            request.user,
            request.POST
        )


        if form.is_valid():

            user = form.save()


            update_session_auth_hash(
                request,
                user
            )


            messages.success(
                request,
                'Password changed successfully.'
            )


            return redirect(
                'staff_portal:profile'
            )


    else:

        form = SupportHubPasswordChangeForm(
            request.user
        )


    return render(
        request,
        'staff_portal/change_password.html',
        {
            'form': form
        }
    )
=======
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def staff_dashboard(request):
    if request.user.role != 'STAFF':
        return redirect('role_redirect')
    return render('staff_dashboard.html')

>>>>>>> 82df279bf52b0f355fac946df2c5d9634d173ff1
