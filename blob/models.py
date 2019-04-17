from django.db import models
from django.contrib.auth import models as auth_models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(auth_models.User)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.png', upload_to='post_image')
    description = models.TextField()

    def __str__(self):
        return self.created.strftime('%d-%m-%y') + '- ' + self.title
