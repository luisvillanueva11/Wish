from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='wishlist'),
    path('create/', views.create, name='create'),
    path('delete/<int:id>', views.delete, name='delete'),
]