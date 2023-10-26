# from django.contrib.auth.backends import ModelBackend
# from .models import User


# class CustomPhoneBackend(ModelBackend):
#     def authenticate(self, request, phone=None, password=None, **kwargs):
#         try:
#             user = User.objects.get(phone=phone)
#         except User.DoesNotExist:
#             return None

#         if user.check_password(password):
#             return user
#         return None



# from django.contrib.auth import get_user_model
# User = get_user_model()

# class AdminPanelBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         try:
#             user = User.objects.get(username=username)
#         except User.DoesNotExist:
#             return None

#         if user.check_password(password):
#             return user
#         return None
