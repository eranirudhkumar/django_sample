from django.db import models


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    joined = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=10, default='')
    password = models.CharField(max_length=16, default='')

    def __str__(self):
        return self.email + " - " + self.phone
