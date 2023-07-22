from datas.models import *
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .functions import *
from django.conf import settings
from .forms import *
def home(request):
    game = Game.objects.all()
    return render(request,'home.html',{"games" : game,"nb": len(game)})

def product(request,game,category,id):
    tab = Product.objects.filter(game__name=game,category__name=category,id=id).get()
    game = Game.objects.filter(name=game).get()
    context = {"tab" : tab, "game": game}
    return render(request,'product.html', context)

def category(request,game,category,page):
    pagination = Product.objects.filter(game__name=game,category__name=category).order_by('-date').all().count()//settings.NB_ITEMS_PER_PAGE
    pagination += 1 if Product.objects.filter(game__name=game,category__name=category).all().count()%settings.NB_ITEMS_PER_PAGE != 0 else 0
    tab = Product.objects.filter(game__name=game,category__name=category).all()[int(page)*settings.NB_ITEMS_PER_PAGE-settings.NB_ITEMS_PER_PAGE:int(page)*settings.NB_ITEMS_PER_PAGE]
    context = {"tab" : tab,"pagination" : pagination, "game": game, "category": category,"current_page": int(page),"paginationm" : int(page) - 1,"paginationp" : int(page) + 1}
    return render(request,'category.html',context)

def game(request,game,page):
    pagination  = Product.objects.filter(game__name=game).order_by('-date').all().count()//settings.NB_ITEMS_PER_PAGE
    pagination += 1 if Product.objects.filter(game__name=game).all().count()%settings.NB_ITEMS_PER_PAGE != 0 else 0
    context = {"tab" : Product.objects.filter(game__name=game).all()[int(page)*settings.NB_ITEMS_PER_PAGE-settings.NB_ITEMS_PER_PAGE:int(page)*settings.NB_ITEMS_PER_PAGE],"game": game,"pagination" : pagination,"current_page": int(page),"paginationm" : int(page) - 1,"paginationp" : int(page) + 1}
    return render(request,'game.html',context)

def search(request,page):
    search = request.GET.get('q')
    tab = Product.objects.filter(name__contains=search).order_by('-date').all()
    pagination = tab.count()//settings.NB_ITEMS_PER_PAGE
    pagination += 1 if tab.count()%settings.NB_ITEMS_PER_PAGE != 0 else 0
    context = {"tab" : tab, "search" : search,"pagination" : pagination,"current_page": int(page),"paginationm" : int(page) - 1,"paginationp" : int(page) + 1}
    return render(request,'search.html',context)
    
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

@staff_member_required
def create_superuser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.is_superuser = True
            user.save()
            return redirect('admin')  
    else:
        form = UserCreationForm()
    return render(request, 'create_superuser.html', {'form': form})

@login_required
def createproduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin')  # Redirect to a success page or desired URL
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})

@staff_member_required
def panel(request):
    return render(request,'panel.html')

####FUNCTIONS SPECIFIC TO WOL####

@staff_member_required
def simplaza(request):
    if request.user.is_superuser:
        return render(request,'simplaza.html')
    else:
        return render(request,'home.html')

@staff_member_required
def aviaworld(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')  # Redirect to a success page or desired URL
    else:
        form = CategoryForm()
    return render(request,'aviaworld.html',{'form': form})

@staff_member_required
def createdaw(request):
    link = request.GET.get('link')
    category = request.GET.get('category')
    title, image, description, changelog, note, url1, url2, game = scrape_aviaworld(link)
    link1,link2 = create_archive(title,url1,game,url2)
    query = Product.objects.create(name=title,game=Game.objects.get(name=game),category=Category.objects.get(name=category),image=image,description=description,changelog=changelog,note=note)
    query.save()
    return render(request,'createdaw.html',{'link': link1,"link2": link2, "original_link": url1,"original_link2": url2})

@staff_member_required
def createdsp(request):
    link = request.GET.get('link')
    flink1 = request.GET.get('flink')
    flink2 = request.GET.get('flink2')
    title, type2, image, description, changelog, note = scrape_simplaza(link)
    query = Product.objects.create(name=title,game=Game.objects.get(name="mfs2020"),category=Category.objects.get(name=type2),image=image,description=description,changelog=changelog,note=note)
    query.save()
    game = "mfs2020"
    if flink2 =="":
        link1,link2 = create_archive(title,flink1, game)
    else:
        link1,link2 = create_archive(title,flink1, game,flink2)
    return render(request,'createdsp.html',{'link': link1,"link2": link2,"original_link": flink1,"original_link2": flink2})

import os

@staff_member_required
def deletearchives(request):
    directory = 'static'  # Chemin vers le dossier 'static'
    for filename in os.listdir(directory):
        if filename.endswith('.zip'):
            file_path = os.path.join(directory, filename)
            os.remove(file_path)
    return render(request,'home.html')

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Automatically log in the user after successful registration
            login(request, user)
            return redirect('/')  # Replace 'home' with the name of your home page URL pattern
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})

def doc(request):
    return render(request,'doc.html')
