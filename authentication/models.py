from datetime import date

from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser

from locations.models import Location


def nine_years_old(value):
    if date.today().year - value.year < 9:
        raise ValidationError("Age must be 9 years old and older")
        

def no_rambler(value):
    domain_name = value.split('@')
    if 'rambler' in domain_name[1]:
        raise ValidationError("No Rambler allowed")


class User(AbstractUser):
    role = models.CharField(max_length=200, default='user')
    age = models.IntegerField(null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    birth_date = models.DateField(null=True, validators=[nine_years_old])
    email_address = models.EmailField(unique=True, validators=[no_rambler])
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']
    
    def __str__(self):
        return self.username
