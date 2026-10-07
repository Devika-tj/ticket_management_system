from django.urls import path
from . import views

urlpatterns = [
    path(
        'support_staff_dashboard/',
        views.support_staff_dashboard,
        name='support_staff_dashboard'
    ),
]
