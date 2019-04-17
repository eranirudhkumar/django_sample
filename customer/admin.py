from django.contrib import admin
from . import models as customer_models

admin.site.register(customer_models.State)
admin.site.register(customer_models.District)
