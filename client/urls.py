from django.conf.urls import url
from . import views as client_views

urlpatterns=[
    url(r'^$', client_views.client_home ,name='client_home'),
    url(r'^register/$', client_views.client_registration ),
]