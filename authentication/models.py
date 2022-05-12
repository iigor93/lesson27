from django.db import models
from django.contrib.auth.models import AbstractUser
from locations.models import Location


class User(AbstractUser):
    role = models.CharField(max_length=200, default='user')
    age = models.IntegerField(null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']
    
    def __str__(self):
        return self.username
