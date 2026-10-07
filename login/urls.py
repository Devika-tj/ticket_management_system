from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import (
    PENLoginView,
    role_redirect,
    staff_dashboard,
    support_dashboard,
    admin_dashboard,
)

urlpatterns = [
    path(
        'login/',
        PENLoginView.as_view(),
        name='login'
    ),

    path(
        'logout/',
        LogoutView.as_view(),
        name='logout'
    ),

    # path(
    #     'dashboard/',
    #     role_redirect,
    #     name='role_redirect'
    # ),

    # path(
    #     'staff/dashboard/',
    #     staff_dashboard,
    #     name='staff_dashboard'
    # ),

    # path(
    #     'support/dashboard/',
    #     support_dashboard,
    #     name='support_dashboard'
    # ),

    # path(
    #     'admin/dashboard/',
    #     admin_dashboard,
    #     name='admin_dashboard'
    # ),
]