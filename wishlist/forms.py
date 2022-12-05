from django.forms import ModelForm
from django import forms
from .models import Wish

class WishForm(ModelForm):

    class Meta:
        model = Wish
        exclude = ('date',)

    image = forms.URLField(
        label='Imagen', 
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'URL de la imagen'}
        )
    )

    product_name = forms.CharField(
        label='Producto', 
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Titulo del producto'}
        )
    )