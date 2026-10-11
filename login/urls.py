from django.urls import path

from .views import (
    change_password,
    profile
)


app_name = 'staff_portal'


urlpatterns = [

    path(
        '',
        profile,
        name='profile'
    ),

    path(
<<<<<<< HEAD
        'change-password/',
        change_password,
        name='change_password'
    ),
=======
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
>>>>>>> 82df279bf52b0f355fac946df2c5d9634d173ff1
]