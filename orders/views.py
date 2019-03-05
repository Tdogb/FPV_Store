from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

def cart(request):
    return render(request, 'orders/cart.html')

@login_required(login_url="/accounts/login/")
def orderList(request):
    return render(request, 'orders/order-list.html')