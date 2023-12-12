from rest_framework import serializers
from .models import *



class loginSerializer(serializers.Serializer):
    phone = serializers.CharField()
    password = serializers.CharField()