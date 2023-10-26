from rest_framework.response import Response
from .models import OTP
import random 
import datetime 

def send_otp(phone):
    otp = random.randint(1000, 9999)
    validity = datetime.datetime.now() + datetime.timedelta(minutes=10)
    OTP.objects.update_or_create(phone = phone, defaults={"otp":otp, "validity":validity, "verified":False})
    
    print(otp)
    return Response("opt send successfully!")