from django.urls import path
from . import views 

urlpatterns = [
    path('request_otp/', views.request_otp, name='request_otp'),
    path('verify_otp/', views.verify_otp, name='verify_otp'),
    path('create_account/', views.create_account, name='create_account'),
    path('login/', views.login_user, name='login_user'),
    path('reset_pass_request/', views.pass_reset_email, name='pass_reset_email'),
]