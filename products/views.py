from django.shortcuts import render
from products.models import Product
from django.shortcuts import *
# Create your views here.

def index(request):
  products= Product.objects.all().order_by('name')
  context= {'products':products}
  return render(request, 'index.html',context)
    
def show(request,product_id):
  obj = get_object_or_404(Product, pk=product_id)
  context= {'product':obj}
 
  return render(request,'show.html',context)