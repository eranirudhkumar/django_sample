from django.conf.urls import url
from . import views as customer_views

urlpatterns = [
    url(r"^$", customer_views.customer_home,
        name='customer_home'),

    url(r"^state/$", customer_views.customer_state,
        name='customer_state')
]
