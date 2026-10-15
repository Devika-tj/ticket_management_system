from django.urls import path

from .views import (
    change_password,
    profile,
    LogoutView
)


app_name = 'staff_portal'


urlpatterns = [

    path(
        '',
        profile,
        name='profile'
    ),

    path(

        'change-password/',
        change_password,
        name='change_password'
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