from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100) 
    
    def __str__(self):
        return self.name
    
class Game(models.Model):
    name = models.CharField(max_length=100,default="Oui")
    has2links = models.BooleanField(default=False)
    link1name = models.CharField(max_length=100,default="Oui")
    link2name = models.CharField(max_length=100,blank=True,null=True)
    picture = models.CharField(max_length=200,default="Oui")
    
    def __str__(self):
        return self.name
    
class Hosters(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100) 
    image = models.CharField(max_length=300) 
    description = models.TextField()
    changelog = models.TextField(blank=True,null=True)
    hostdownload = models.ForeignKey(Hosters, on_delete=models.CASCADE, default=1)
    download = models.CharField(max_length=300)
    hostdownload2 = models.ForeignKey(Hosters, on_delete=models.CASCADE, default=1, related_name='hostdownload2')
    download2 = models.CharField(max_length=300,blank=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    note = models.CharField(max_length=1000, blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if CatAndGames.objects.filter(game=self.game, category=self.category).exists():
            pass
        else :
            CatAndGames(game=self.game, category=self.category).save()
            
        super(Product, self).save(*args, **kwargs)
    

class CatAndGames(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.category.name
    

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    discord = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.username
    

    

    