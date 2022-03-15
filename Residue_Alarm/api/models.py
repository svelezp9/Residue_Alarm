from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password

class UserProfileManager(BaseUserManager):
    '''Manager para perfiles de usuario'''
    def create_user(self,email,name,password):
        if not email:
            raise ValueError('El Usuario debe tener email')
        email = self.normalize_email(email)
        user = self.model(email=email,name=name)

        user.password = make_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,password):
        user = self.create_user(email,name,password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self.db)

        return user

class UserProfile(AbstractBaseUser,PermissionsMixin):
    ''' Modelo Base de datos para usuarios en el sistema'''
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS  = ['name']

    def __str__(self):
        '''Retorna cadena representando a nuestro usuario'''
        return self.email


