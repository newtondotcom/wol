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
    changelog = models.CharField(max_length=100, blank=True,null=True)
    download = models.CharField(max_length=300)
    hostdownload = models.ForeignKey(Hosters, on_delete=models.CASCADE, default=1)
    download2 = models.CharField(max_length=300,blank=True)
    hostdownload2 = models.ForeignKey(Hosters, on_delete=models.CASCADE, default=1, related_name='hostdownload2')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    note = models.CharField(max_length=1000, blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)

class CatAndGames(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.category.name
    

    

    