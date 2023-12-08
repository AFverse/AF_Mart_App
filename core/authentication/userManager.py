from django.contrib.auth.models import AbstractBaseUser

class UserManager(AbstractBaseUser):
    def create_user(self, email, password=None, **extra):

        user = self.model(phone = self.phone, password = password)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra):

        email = self.normalize_email(email)
        user = self.create_user(email,password)
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user