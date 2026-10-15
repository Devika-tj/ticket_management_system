from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [

    path(
        'django-admin/',
        admin.site.urls
    ),

    path(
        '',
        include('login.urls')
    ),

    path(
        'tickets/',
        include('tickets.urls')
    ),

    path(
        'profile/',
        include('staff_portal.urls')
    ),

    path(
        'support/',
        include('support_staff.urls')
    ),

    path(
        'admin-panel/',
        include('admin_app.urls')
    ),
]


if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
    

    

from django.urls import path
from . import views

urlpatterns = [
    path(
        'support_staff_dashboard/',
        views.support_staff_dashboard,
        name='support_staff_dashboard'
    ),
]

