<<<<<<< HEAD
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.http import JsonResponse

from django.shortcuts import (
    get_object_or_404,
    redirect,
    render
)


from .forms import (
    TicketCommentForm,
    TicketForm
)

from .models import (
    RequestType,
    Ticket,
    TicketAttachment
)


@login_required
def my_tickets(request):

    tickets = (
        Ticket.objects
        .filter(
            created_by=request.user
        )
        .select_related(
            'department',
            'request_type'
        )
    )


    status = request.GET.get(
        'status',
        'all'
    )


    query = request.GET.get(
        'q',
        ''
    ).strip()


    if status in {
        'open',
        'in_progress',
        'resolved'
    }:

        tickets = tickets.filter(
            status=status
        )


    if query:

        tickets = (
            tickets.filter(
                title__icontains=query
            )
            |
            tickets.filter(
                ticket_no__icontains=query
            )
        )


    return render(
        request,
        'tickets/my_tickets.html',
        {
            'tickets': tickets,
            'active_status': status,
            'query': query
        }
    )


@login_required
def create_ticket(request):

    if request.method == 'POST':

        form = TicketForm(
            request.POST,
            request.FILES
        )


        if form.is_valid():

            ticket = form.save(
                commit=False
            )


            ticket.created_by = request.user

            ticket.save()


            for f in request.FILES.getlist(
                'attachments'
            ):

                TicketAttachment.objects.create(
                    ticket=ticket,
                    file=f
                )


            messages.success(
                request,
                'Ticket created successfully!'
            )


            return redirect(
                'tickets:detail',
                ticket_no=ticket.ticket_no
            )


    else:

        form = TicketForm()


    return render(
        request,
        'tickets/create.html',
        {
            'form': form
        }
    )


@login_required
def request_types_api(request):

    department_id = request.GET.get(
        'department'
    )


    rows = (
        RequestType.objects
        .filter(
            department_id=department_id,
            is_active=True
        )
        .values(
            'id',
            'name'
        )
        if department_id
        else []
    )


    return JsonResponse(
        list(rows),
        safe=False
    )


@login_required
def ticket_detail(
    request,
    ticket_no
):

    ticket = get_object_or_404(

        Ticket.objects
        .select_related(
            'department',
            'request_type',
            'created_by',
            'assigned_to'
        )
        .prefetch_related(
            'attachments',
            'comments__author'
        ),

        ticket_no=ticket_no,

        created_by=request.user
    )


    if request.method == 'POST':

        form = TicketCommentForm(
            request.POST
        )


        if form.is_valid():

            c = form.save(
                commit=False
            )


            c.ticket = ticket

            c.author = request.user

            c.save()


            return redirect(
                'tickets:detail',
                ticket_no=ticket.ticket_no
            )


    else:

        form = TicketCommentForm()


    return render(
        request,
        'tickets/detail.html',
        {
            'ticket': ticket,
            'comment_form': form
        }
    )
=======
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


>>>>>>> 82df279bf52b0f355fac946df2c5d9634d173ff1
