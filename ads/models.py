from django.db import models
from authentication.models import User
from categories.models import Categories

    
class Ads(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price = models.IntegerField()
    description = models.CharField(max_length=2000)
    is_published = models.BooleanField()
    image = models.ImageField(upload_to='media/', null=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    
    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
    
    def __str__(self):
        return self.name
    

    
