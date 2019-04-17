from django.conf.urls import url
# from django.contrib.auth.views import login
from django.contrib.auth import views as auth_view
from . import views

urlpatterns=[
# http://127.0.0.1:8000/account/ => account_home
    url(r'^$', views.account_home, name='account_home'),

    # url(r'^login/$', login, {'template_name': 'account/login.html'}, name='account_login'),
    url(r'^login/$', auth_view.login, {'template_name': 'account/login.html'}, name='account_login'),
    url(r'^logout/$', auth_view.logout,{'template_name': 'account/logout.html'}, name='account_logout'),
]