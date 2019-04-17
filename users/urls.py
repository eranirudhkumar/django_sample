from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.home, name='users_home'),
    url(r'^login/$', views.users_login, name='users_login'),
    url(r'^register/$', views.users_registration, name='users_regiter'),
    url(r'^edit/$', views.users_change, name='users_edit'),
    url(r'^users/$', views.users_users, name='users_users'),
    url(r'^otp/$', views.otp_validation, name='users_otp'),
]