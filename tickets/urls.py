from django.urls import path
<<<<<<< HEAD

from . import views


app_name = 'tickets'


urlpatterns = [

    path(
        '',
        views.my_tickets,
        name='my_tickets'
    ),

    path(
        'create/',
        views.create_ticket,
        name='create'
    ),

    path(
        'request-types/',
        views.request_types_api,
        name='request_types'
    ),

    path(
        '<int:ticket_no>/',
        views.ticket_detail,
        name='detail'
    ),
=======
from . import views

urlpatterns = [
    path('tickets/', views.ticket_list, name='ticket_list'),
    path('ticket/<int:pk>/', views.ticket_detail, name='ticket_detail'),

>>>>>>> 82df279bf52b0f355fac946df2c5d9634d173ff1
]