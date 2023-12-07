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
