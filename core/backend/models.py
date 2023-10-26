from django.db import models

class User(models.Model):
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    fullname = models.CharField(max_length=100)
    password = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    
class OTP(models.Model):
    phone = models.CharField(max_length=9)
    otp = models.IntegerField()
    validity = models.DateTimeField()
    verified = models.BooleanField(default=False)
    
    def __str__(self):
        return self.phone 
    