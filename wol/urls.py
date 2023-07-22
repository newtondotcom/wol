from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home ),
    path('product/<game>/<category>/<id>', product),
    path('category/<game>/<category>/<page>', category),
    path('game/<game>/<page>', game),
    path('search/<page>/', search),
    path('simplaza/', simplaza),
    path('create_superuser/', create_superuser),
    path('aviaworld', aviaworld),
    path('createproduct/', createproduct),
    path('panel/', panel),
    path('createdsp/', createdsp),
    path('createdaw/', createdaw),
    path('deletearchives/', deletearchives),
    path('accounts/register/', register),
    path('doc/', doc),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]