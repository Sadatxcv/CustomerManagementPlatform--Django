from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    
    total_orders = orders.count()
    total_customers = customers.count()
    delivered= orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()  
    
    context = {'orders':orders, 'customers':customers, 'total_orders':total_orders, 'pending':pending, 'delivered':delivered, 'total_customers':total_customers}
    
    return render(request,'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    return render(request,'accounts/products.html', {'products': products})

def customers(request):
    return render(request,'accounts/customer.html')