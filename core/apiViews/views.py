from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import views 
from rest_framework.response import Response
from backend.models import *

from .serializers import categorySerializer

class categoriesViews(views.APIView):
    
    def get(self, request):
        pCategories = ParentCategory.objects.all()
        serializer = categorySerializer(pCategories, many = True)
        
        return Response(serializer.data, status=200)

