from django.urls import path
from . import views 

urlpatterns = [
    path('alert/', views.alert, name='alert'),
    path('requestOtp/', views.requestOtp, name='requestOtp'),
    path('verifyOtp/<phone>', views.verifyOtp, name='verifyOtp'),
    path('createAccount/<phone>', views.createAccount, name='createAccount'),
    path('login/', views.login_user, name='login_user'),
    path('reset_pass_request/', views.pass_reset_email, name='pass_reset_email'),
    path('reset_pass_form/<email>/<token>/', views.reset_pass_form, name='reset_pass_form'),
    path('reset_pass_confirm/', views.reset_pass_confirm, name='reset_pass_confirm'),
    path('userdata/', views.userdata, name='userdata'),
    path('celery/', views.test, name='celery'),
    
  
]