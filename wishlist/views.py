from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Wish
from .forms import WishForm

def index(request):
    wishes = Wish.objects.all()
    context = {
        'wishes': wishes
    }
    return render(request, 'wishlist/index.html', context)

def create(request):
    if request.method == 'GET':
        form = WishForm()
        context = {
            'form': form
        }
        return render(request, 'wishlist/create.html', context)
    
    if request.method == 'POST':
        form = WishForm(request.POST)
        if form.is_valid:
            form.save()
        context = {
            'form': form
        }
        messages.success(request, 'Producto creado correctamente')
        return redirect('wishlist')

def delete(request, id):
    wish = Wish.objects.get(id=id)
    wish.delete()
    return redirect('wishlist')