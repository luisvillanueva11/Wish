from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Wish

def index(request):
    wishes = Wish.objects.all()
    context = {
        'wishes': wishes
    }
    return render(request, 'wishlist/index.html', context)

def create(request):
    HttpResponse('Probando crear')

def delete(request, id):
    wish = Wish.objects.get(id=id)
    wish.delete()
    return redirect('wishlist')