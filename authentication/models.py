# from django.db import models
# from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager
#
#
# class UserManager(BaseUserManager):
#     def create_user(self, email, password, **extra_fields):
#         if not email:
#             raise ValueError('The E-Mail is not given.')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user
#
#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault('is_staff', 'True')
#         extra_fields.setdefault('is_superuser', 'True')
#         extra_fields.setdefault('is_active', 'True')
#
#         if not extra_fields.get('is_staff'):
#             raise ValueError('SuperUser must have is_staff = True')
#
#         if not extra_fields.get('is_superuser'):
#             raise ValueError('SuperUser must have is_superuser= True')
#
#         return self.create_user(email, password, **extra_fields)
#
#
# class CustomUser(AbstractBaseUser):
#     email = models.EmailField(max_length=50, null=True, unique=True)
#     username = models.CharField(max_length=50, null=True, blank=True)
#     password = models.CharField(max_length=50, null=True)
#     first_name = models.CharField(max_length=100, null=True, blank=True)
#     last_name = models.CharField(max_length=100, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']
#
#     objects = UserManager()
#
#     def __str__(self):
#         return self.email
#
#     def has_module_perms(self, app_label):
#         return True
#
#     def has_perm(self, perm, obj=None):
#         return True
#

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password,check_password

class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(user.password)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        superuser = self.model(email=email, **extra_fields)

        superuser.set_password(password)
        superuser.is_superuser = True
        superuser.is_staff = True
        superuser.save()
        return superuser


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_superuser = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return self.first_name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email

class User_Authentication(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)