from django import forms
from .models import Product  # Capitalized the model name

class ProductForm(forms.Form):

    name = forms.CharField(max_length=55)
    color = forms.CharField(max_length=25)
    sku = forms.CharField(max_length=25)
    price = forms.FloatField()

    # class Meta:
    #     model = Product
    #     fields = ('name', 'color', 'sku', 'price')
