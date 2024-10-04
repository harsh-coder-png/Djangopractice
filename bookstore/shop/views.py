from itertools import product
from django.shortcuts import render
from . models import Product

# Create your views here.
def home(req):
    context = {}
    products = Product.objects.all()
    context['Product'] = products
    return render(req,'shop/home.html',context)

def search(req):
    context = {}
    if req.method == 'POST':
        book_name = req.Post['book_name']
        print(book_name)
        Product=product.objects.filter(book_name_contains = book_name)
        context['Product'] = product
    return render(req,'shop/search.html',context)
