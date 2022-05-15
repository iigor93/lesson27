from django.db import models
from django.core.validators import MinLengthValidator

class Categories(models.Model):
    name = models.CharField(max_length=20)
    slug = models.CharField(unique=True, max_length=10, validators=[MinLengthValidator(5)])
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.name
    
