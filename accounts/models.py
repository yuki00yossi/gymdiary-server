from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils import timezone


# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(
            self, email, username, disp_name, password=None, **extra_fields):
        if not email or not username or not disp_name:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            disp_name=disp_name,
            **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
            self, email, username, disp_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        print('------------------------------')
        print(email, username, disp_name)
        print(extra_fields)
        print('------------------------------')
        return self.create_user(
            email, username, disp_name, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    username = models.CharField(
        unique=True, verbose_name='username', max_length=32)
    disp_name = models.CharField(verbose_name='disp_name', max_length=256)
    is_trainer = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email', 'disp_name',]

    class Meta:
        verbose_name = 'User'
