from django.db import models

from authentication.models import User
from ads.models import Ads


class Selection(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    ads = models.ManyToManyField(Ads)
    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = "Подборка"
        verbose_name_plural = "Подборки"
    
