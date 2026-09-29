from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def staff_dashboard(request):
    if request.user.role != 'SUPPORT':
        return redirect('role_redirect')
    return render('support/support_dashboard.html')
