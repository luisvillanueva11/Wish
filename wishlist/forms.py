from django.forms import ModelForm
from django import forms
from .models import Wish

class WishForm(ModelForm):
    class Meta:
        model = Wish
        exclude = ('date',)

        widget = {
            'image' : forms.TextInput(attrs={'placeholder':'Prueba'})
        }