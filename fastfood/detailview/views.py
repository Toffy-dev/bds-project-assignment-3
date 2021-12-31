from django.shortcuts import render, redirect
from main.models import *
from django.contrib.auth.decorators import user_passes_test
# Create your views here.

@user_passes_test(lambda u: u.is_superuser, login_url='/')
def order(response):
    orders = Order_menu.objects.select_related('customer', 'address')
    #orders = Order_menu.objects.all()
    return render(response, "detailview/orderview.html", {'orders': orders})

