from django.urls import path
from . import views 

urlpatterns = [
    path('getCategories/', views.categoriesViews.as_view(), name="getCategories")
]