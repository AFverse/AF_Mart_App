from django.urls import path
from .views import *



urlpatterns = [
    path('getCategories/', categoriesViews.as_view(), name="getCategories"),
    path('getProducts/', productViews.as_view(), name="getProducts"),
]
   