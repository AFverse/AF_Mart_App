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
    product_info = productSerializer(source='product', read_only=True)
    class Meta:
        model = CartItmes
        fields = '__all__'
        

class orderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = '__all__'
        

class orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class orderItemSerializer(serializers.ModelSerializer):
    product_info = productSerializer(source='product', read_only=True)
    class Meta:
        model = OrderItems
        fields = '__all__'

class productReviewsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Reviews
        fields = '__all__'

class brandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'

        

        
        