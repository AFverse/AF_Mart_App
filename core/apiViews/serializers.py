from rest_framework import serializers
from backend.models import *

class categorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ParentCategory
        fields = '__all__'
        


class subCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class cartItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItmes
        fields = '__all__'
        

        
        