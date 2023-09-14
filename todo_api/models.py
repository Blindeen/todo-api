from django.db import models
from django.contrib.auth.models import AbstractUser

class UserData(AbstractUser):
    username = None
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name


class List(models.Model):
    header = models.CharField(max_length=20)

    user = models.ForeignKey(UserData, on_delete=models.CASCADE)


class Task(models.Model):
    description = models.CharField(max_length=100)
    is_done = models.BooleanField(default=False)

    list = models.ForeignKey(List, on_delete=models.CASCADE)
