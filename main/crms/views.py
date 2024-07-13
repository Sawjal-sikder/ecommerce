from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

# Create your views here.
def product_view(request):  # Renamed the view to avoid conflict with the model
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            color = form.cleaned_data['color']
            sku = form.cleaned_data['sku']
            price = form.cleaned_data['price']
            Productlinfo = Product(name=name, color=color, sku=sku, price=price)
            Productlinfo.save()
            return redirect('success')

    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})

def success(request):
    return render(request, 'success.html')  # Render the success template
