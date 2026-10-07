from django.shortcuts import render,get_object_or_404
from .models import Ticket



def ticket_list(request):
    user = request.user
    
    if user.is_superuser or user.is_staff:
        tickets = Ticket.objects.all()
        

    else:
        tickets = Ticket.objects.filter(creator=user)
        
    return render(request, 'tickets/ticket_list.html', {'tickets': tickets})


def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    
    if not (request.user.is_superuser or request.user.is_staff or ticket.creator == request.user):
        from django.http import HttpResponseForbidden
        return HttpResponseForbidden("You do not have permission to view this ticket.")
        
    return render(request, 'tickets/ticket_details.html', {'ticket': ticket})

def staff_dashboard(request):

    tickets = Ticket.objects.filter(staff=request.user)
    return render(request, 'staff_dashboard.html', {'tickets': tickets})


