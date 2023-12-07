from django.urls import path
from .views import *



urlpatterns = [
    path('getCategories/', categoriesViews.as_view(), name="getCategories"),
    path('getCategories/<int:id>/', categoriesViews.as_view(), name="getCategoriesWithId"),
]
   