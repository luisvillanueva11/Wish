from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wishlist/', include('wishlist.urls')),
    path('', views.index, name='index'),
]
