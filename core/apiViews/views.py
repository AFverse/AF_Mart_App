from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import views 
from rest_framework.response import Response
from backend.models import *

from .serializers import *

class categoriesViews(views.APIView):
    
    def get(self, request):

        pCategories = ParentCategory.objects.all()
        serializer = categorySerializer(pCategories, many = True)
        return Response(serializer.data, status=200)

  

    def post(self, request, *args, **kwargs):

        id = self.request.data.get('id')
        if id is not None:

            pc=ParentCategory.objects.get(id=id)
            subCategories=pc.subCat.all()
            serializer = subCatSerializer(subCategories, many = True)
            return Response({'status':200, 'message':'These are producs sub categories according to parent category', 'payload': serializer.data})
        
        else:
            return HttpResponse('input valid id please')