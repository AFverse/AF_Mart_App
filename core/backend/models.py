from django.db import models

class User(models.Model):
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    fullname = models.CharField(max_length=100)
    password = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.phone
    
class OTP(models.Model):
    phone = models.CharField(max_length=9)
    otp = models.IntegerField()
    validity = models.DateTimeField()
    verified = models.BooleanField(default=False)
    
    def __str__(self):
        return self.phone
    
class Token(models.Model):
    token = models.CharField(max_length=5000) 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Tokens_set')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.user.phone
    
    
class PassResetToken(models.Model):
    token = models.CharField(max_length=5000) 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pass_reset_tokens_set')
    validity = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.user.phone
    