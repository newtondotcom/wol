from django.contrib import admin
from .models import CatAndGames, Category, Game, Hosters, Product

@admin.register(CatAndGames)
class CatAndGamesAdmin(admin.ModelAdmin):
    list_display = ('game','category')
    list_filter = ('category',)
    search_fields = ('game__name','category__name')
    ordering = ('game__name','category__name')
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
@admin.register(Game)
class GamesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
@admin.register(Hosters)
class HostersAdmin(admin.ModelAdmin):
     list_display = ('name',)
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'changelog', 'download', 'download2')