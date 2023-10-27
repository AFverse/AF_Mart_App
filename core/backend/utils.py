import uuid
from rest_framework.response import Response
from .models import *
import random 
import datetime


def send_otp(phone):
    otp = random.randint(1000, 9999)
    validity = datetime.datetime.now() + datetime.timedelta(minutes=10)
    OTP.objects.update_or_create(phone = phone, defaults={"otp":otp, "validity":validity, "verified":False})
    
    print(otp)
    return Response("opt send successfully!")


def new_token():
    token = uuid.uuid1().hex 
    print(token)
    return token

def token_response(user):
    token = new_token()
    Token.objects.create(token = token, user = user)
    return Response(f"token {token}")

    