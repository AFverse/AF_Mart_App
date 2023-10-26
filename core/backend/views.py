import datetime
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import User, OTP 
from django.contrib.auth.hashers import make_password
from .utils import send_otp
from django.contrib.auth import authenticate, login

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

    if not phone or not password:
        return Response({'error': 'Phone number and password are required'}, status=status.HTTP_BAD_REQUEST)

    # user = authenticate(request, phone=phone, password=password)
    try:
            user = User.objects.get(phone=phone)
    except User.DoesNotExist:
            return Response("user does not exist")

    if user is not None and user.check_password(password):
        login(request, user)
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_UNAUTHORIZED)
