from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=20)
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.name
    
    
class Ads(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey('UserClass', on_delete=models.CASCADE, null=True)
    price = models.IntegerField()
    description = models.CharField(max_length=2000)
    is_published = models.BooleanField()
    image = models.ImageField(upload_to='media/', null=True)
    category = models.ForeignKey('Categories', on_delete=models.CASCADE, null=True)
    
    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
    
    def __str__(self):
        return self.name
    
    
class Location(models.Model):
    name = models.CharField(max_length=200)
    lat = models.CharField(max_length=200)
    lng = models.CharField(max_length=200)
    
    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'
    
    def __str__(self):
        return self.name
    

class UserClass(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    age = models.IntegerField()
    location = models.ForeignKey('Location', on_delete=models.CASCADE, null=True)
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']
    
    def __str__(self):
        return self.username
