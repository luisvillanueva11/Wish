from django.shortcuts import render
from django.http import HttpResponse
from .models import Wish

def index(request):
    wishes = Wish.objects.all()
    context = {
        'wishes': wishes
    }
    return render(request, 'wishlist/index.html', context)