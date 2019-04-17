from django.contrib import admin
from . import models as blog_models
# Register your models here.

admin.site.register(blog_models.Post)