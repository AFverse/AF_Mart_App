import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import User, OTP 
from django.contrib.auth.hashers import make_password
from .utils import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.contrib import messages



@api_view(['GET'])
def alert(request):
    return render(request, 'alert.html')

@api_view(['POST'])
def request_otp(request):
    phone = request.data.get('phone')
    
    if phone:
        if User.objects.filter(phone = phone).exists():
            return Response("Phone already exists!", status=400)
        return send_otp(phone)    
    
    else:
        return Response("data_missing", status=400)


@api_view(['POST'])
def verify_otp(request):
    phone = request.data.get('phone')
    otp = request.data.get('otp')
    
    otp_obj = get_object_or_404(OTP, phone = phone, verified = False)
    
    if otp_obj.validity.replace(tzinfo=None) > datetime.datetime.utcnow():
        if otp_obj.otp == int(otp):
            otp_obj.verified = True 
            otp_obj.save()
            return Response("otp_verified_successfully!")
        return Response("otp_not_matched!", status=400)
            
    else:
        return Response('otp_expired', status=400)
    
    
@api_view(['POST'])
def create_account(request):
    phone = request.data.get('phone')
    email = request.data.get('email')
    fullname = request.data.get('fullname')
    password = request.data.get('password')
    
    otp_obj = get_object_or_404(OTP, phone = phone, verified = True)
    otp_obj.delete()
    
    User.objects.create(phone = phone, email = email, fullname = fullname, password = make_password(password))
    return Response("account_created_successfully!")
    

@api_view(['POST'])
def login_user(request):
    phone = request.data.get('phone')
    password = request.data.get('password')
    email = request.data.get('email')
    
    if email:
        user = get_object_or_404(User, email = email)
        
    elif phone:
        user = get_object_or_404(User, phone = phone)
    else:
        return Response("data_missing", 400)
    
    if check_password(password, user.password):
        return token_response(user)
    else:
        return Response("incorrect_password", 400)

    

@api_view(['POST'])
def pass_reset_email(request):
    phone  = request.data.get('phone')
    email  = request.data.get('email')
    
    if phone:
        user = get_object_or_404(User, phone = phone)
        return send_pass_reset_email(user)
    elif email:
        user = get_object_or_404(User, email = email)
        return send_pass_reset_email(user)
    else:
        return Response("data missing!", 400)
    
    
@api_view(['GET'])
def reset_pass_form(request, email, token):
    token_instance = PassResetToken.objects.filter(user__email = email, token = token).first()
    
    if token_instance:
        if datetime.datetime.utcnow() < token_instance.validity.replace(tzinfo=None):
            context = {
                'email':email,
                'token':token,
                # 'base_url':TEMPLATES_BASE_URL,
            }
            return render(request, 'accounts/new-pass-form.html', context)
        else:
            token_instance.delete()
            messages.error(request, 'Linked Expired')
            return redirect('alert')
    else:
        messages.info(request, "Instance Not found!")
        return redirect('alert')
    
@api_view(['POST'])
def reset_pass_confirm(request):
    password1 = request.data.get('password1')
    password2 = request.data.get('password2')
    email = request.data.get('email')
    token = request.data.get('token')
    token_instance = PassResetToken.objects.filter(user__email = email, token = token).first()
    
    if token_instance:
        if datetime.datetime.utcnow() < token_instance.validity.replace(tzinfo=None):
            if password1 == password2:
                user = token_instance.user 
                user.password = make_password(password1)
                user.save()
                token_instance.delete()
                Token.objects.filter(user = user).delete()
                messages.success(request, "Password Updated successfully!")
                return redirect('alert')
            else:
                context = {
                'email':email,
                'token':token,
                'error': "Passowrd and confirm password must be same!",
                }
            return render(request, 'accounts/new-pass-form.html', context)
    
    else:
        messages.error(request, 'Linked Expired')
        return redirect('alert')
    
@api_view(['GET'])
@permission_classes([IsAuthenticatedUser])
def userdata(request):
    return Response()


def Categories(request):
    return render(request, 'categories.html')

def ProductByCtg(request):
    return render(request, 'productsByCtg.html')

def ProductDetails(request, id):
    return render(request, 'product_details.html', {'id':id})
    
    