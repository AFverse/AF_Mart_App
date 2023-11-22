import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import User, OTP 
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from .models import *


def Categories(request):
    pCat=ParentCategory.objects.all()
    context={'pCat' : pCat}
    return render(request, 'categories.html', context)


def ProductByCtg(request, id):
    obj = Product.objects.filter(category__id=id)
    context={'products':obj}
    return render(request, 'productsByCtg.html', context)

def ProductDetails(request, id):
    obj=Product.objects.get(id=id)
    context={'product':obj}
    print(obj.disc)
    return render(request, 'product_details.html', context)
    