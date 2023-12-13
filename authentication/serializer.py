from rest_framework import serializers    
from .models import *
from django.contrib.auth import get_user_model
User = get_user_model()



from rest_framework import serializers
from .models import cUser  # Update the import

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = cUser  # Use your custom user model
        fields = ('first_name', 'last_name', 'email', 'phone', 'password', 'password2')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.pop('password2', None)

        if password != password2:
            raise serializers.ValidationError('Password and confirm password do not match!')

        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password')
        password2 = validated_data.pop('password2')
       

        if password != password2:
            raise serializers.ValidationError

        user = cUser(**validated_data)
        user.set_password(password)  

       
        user.save()

        return user


  

   





# class UserRegistrationSerializer(serializers.ModelSerializer):
#     password2 = serializers.CharField(write_only=True, style={'input_type': 'password'})

#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email', 'phone', 'password', 'password2')
#         extra_kwargs = {'password': {'write_only': True}}

#     def validate(self, attrs):
#         password = attrs.get('password')
#         password2 = attrs.pop('password2', None)  # Remove password2 from the validated data

#         if password != password2:
#             raise serializers.ValidationError('Password and confirm password do not match!')

#         return attrs
 
#     def create(self, validated_data):
#         return User.objects.create_user(**validated_data)




# class loginSerializer(serializers.Serializer):
#     phone = serializers.CharField()
#     password = serializers.CharField()