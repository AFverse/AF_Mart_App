from rest_framework import serializers
from .models import cUser


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField( style = {'input_type':'password'}, write_only = True)
    class Meta:
        model = cUser
        fields = ['phone', 'email', 'password', 'password2']
                  

    def validate(self, attrs):
        password1 = attrs['password']
        password2 = attrs['password2']
        print("Password1:", password1)
        print("Password2:", password2)

        if password1 and password2 and password1 != password2:
            raise serializers.ValidationError("Your entered passwords doesn't match!")
        
        max_size = 3 * 1024 * 1024  # 3 MB in bytes        
        image = attrs.get('image')
        if image and image.size > max_size:
            raise serializers.ValidationError("Image size should not exceed 1 MB.")
        
          # Check if the file has a valid image extension
        allowed_extensions = ['.jpg', '.jpeg', '.png']
        if image and not any(image.name.lower().endswith(ext) for ext in allowed_extensions):
            raise serializers.ValidationError("Invalid file format. Please upload a .jpg, .jpeg, or .png file.")
        
        return super().validate(attrs)


    def create(self, validated_data):
       
        return cUser.objects.create_user(**validated_data)

class userLoginSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=100)
    class Meta:
        model = cUser
        fields = ['phone', 'password']

class userProfileViewSerializer(serializers.ModelSerializer):
    class Meta:
      model = cUser
      fields = ['first_name','last_name', 'phone', 'email', 'date_of_birth', 'image', 'last_login']
