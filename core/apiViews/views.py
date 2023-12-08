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
        ctg_id = self.request.data.get('ctg_id')
        if id is not None:
            pc=ParentCategory.objects.get(id=id)
            subCategories=pc.subCat.all()
            serializer = subCatSerializer(subCategories, many = True)
            return Response({'status':200, 'message':'These are producs sub categories according to parent category', 'payload': serializer.data})
        
        if ctg_id is not None:
            ctg=Category.objects.get(id=ctg_id)
            products = ctg.products.all()
            serializer = productSerializer(products, many = True)
            return Response({'status':200, 'message':'These are products according to the category', 'payload': serializer.data})
        
        else:
            return Response({'message': 'input valid id please'})
        
class productViews(views.APIView):
    
    def get(self, request, *args, **kwargs):
        topSell = self.request.query_params.get('topSell')
        recommended = self.request.query_params.get('recommended')
        featured = self.request.query_params.get('featured')
        
        products = Product.objects.all()[:10]
        if topSell:
            products = Product.objects.filter(top_selling = True)
            
        if recommended:
            products = Product.objects.filter(is_recommended = True)
    
        if featured:
            products = Product.objects.filter(is_featured = True)
        
        serializer = productSerializer(products, many = True)
        return Response({ 'status': 200, 'message': 'These are products', 'payload': serializer.data })
        
    
    def post(self, request, *args, **kwargs):

        slg = self.request.data.get('slug')
        try:
            obj = Product.objects.get(slug = slg)
        except Exception as e:
            print("Error to get product by slug", e) 
        serializer = productSerializer(obj)
        return Response({ 'status': 200, 'message': 'These are products', 'payload': serializer.data })