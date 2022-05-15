from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator

from authentication.models import User
from categories.models import Categories

    
class Ads(models.Model):
    name = models.CharField(max_length=200, validators=[MinLengthValidator(10)])
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price = models.IntegerField(validators=[MinValueValidator(0)])
    description = models.CharField(max_length=2000, null=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='media/', null=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    
    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['name']
    
    def __str__(self):
        return self.name
    

    
