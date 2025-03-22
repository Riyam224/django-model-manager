from django.shortcuts import render

# Create your views here.
from .models import Product


# todo return product based on method in model manager 
def product(request):
    product  =  Product.objects.get_available_product()
    return render(request, 'index.html', {'product': product})
     
    