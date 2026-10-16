from django.urls import path

from .views import (
    PasswordChangeView ,
    # profile,
    LogoutView
)


app_name = 'staff_portal'


urlpatterns = [

    # path(
    #     '',
    #     # profile,
    #     name='profile'
    # ),

     path('change-password/', PasswordChangeView.as_view(), name='change_password'),


    path(
        'logout/',
        LogoutView.as_view(),
        name='logout'
    ),

   
]