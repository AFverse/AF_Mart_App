# from django.contrib.auth.models import AbstractBaseUser

# class UserManager(AbstractBaseUser):
#     def create_user(self, phone , password=None, **extra):

#         user = self.model(phone = self.phone, password = password)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra):

#         email = self.normalize_email(email)
#         user = self.create_user(email,password)
#         user.is_admin = True
#         user.is_active = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user




from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, phone, password=None):
        user = self.model(phone=phone)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra):
        user = self.create_user(phone, password=password)
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
