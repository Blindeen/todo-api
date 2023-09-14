from django.db import models
from django.contrib.auth.models import AbstractUser

class UserData(AbstractUser):
    NAME_MAX_LEN = 100
    EMAIL_MAX_LEN = 100

    username = None
    name = models.CharField(max_length=NAME_MAX_LEN, unique=True)
    email = models.EmailField(max_length=EMAIL_MAX_LEN, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name


class List(models.Model):
    HEADER_MAX_LEN = 20

    header = models.CharField(max_length=HEADER_MAX_LEN)
    user = models.ForeignKey(UserData, on_delete=models.CASCADE)


class Task(models.Model):
    DESCRIPITON_MAX_LEN = 100

    description = models.CharField(max_length=DESCRIPITON_MAX_LEN)
    is_done = models.BooleanField(default=False)

    list = models.ForeignKey(List, on_delete=models.CASCADE)
