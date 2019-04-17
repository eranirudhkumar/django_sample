from django.conf.urls import url
from .views import (home,
                    add_student,
                    login_student)
from .views import HomeView, StudentApiView

urlpatterns = [
    url(r'^$', home, name='app_home'),
    url(r'^add-student/$', add_student, name='app_add_student'),
    url(r'^login-student/$', login_student, name='app_login-student'),

    url(r'^home/$',
        HomeView.as_view(
            template_name='myapp/home.html'
        ),
        name='myapp_home'),
    url(r'^api/$', StudentApiView.as_view())
]
