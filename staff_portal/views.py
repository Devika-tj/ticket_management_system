from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def staff_dashboard(request):
    if request.user.role != 'STAFF':
        return redirect('role_redirect')
    return render('staff_dashboard.html')

