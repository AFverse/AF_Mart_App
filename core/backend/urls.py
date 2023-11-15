from django.urls import path
from . import views 

urlpatterns = [
    path('alert/', views.alert, name='alert'),
    path('request_otp/', views.request_otp, name='request_otp'),
    path('verify_otp/', views.verify_otp, name='verify_otp'),
    path('create_account/', views.create_account, name='create_account'),
    path('login/', views.login_user, name='login_user'),
    path('reset_pass_request/', views.pass_reset_email, name='pass_reset_email'),
    path('reset_pass_form/<email>/<token>/', views.reset_pass_form, name='reset_pass_form'),
    path('reset_pass_confirm/', views.reset_pass_confirm, name='reset_pass_confirm'),
    path('userdata/', views.userdata, name='userdata'),
    
    
    path('categories/', views.Categories, name='categories'),
    path('product_by_ctg/', views.ProductByCtg, name='product_by_ctg'),
    path('product_details/<id>/', views.ProductDetails, name='product_details'),
    
]