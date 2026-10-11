<<<<<<< HEAD
=======
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tickets.models import Ticket

@login_required
def support_staff_dashboard(request):
    if request.user.role != 'SUPPORT':
        return redirect('role_redirect')
    return render('support_staff_dashboard.html')

context={
    'open_count':
      Ticket.objects.filter(status='open').count(),
      'progress_count':
      Ticket.objects.filter(status='progress').count(),
      'Resolved_count':
      Ticket.objects.filter(status='Resolved').count()
}

    
>>>>>>> 82df279bf52b0f355fac946df2c5d9634d173ff1
