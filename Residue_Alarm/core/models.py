from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager , PermissionsMixin
from django.conf import settings
# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self,email,password,**extra_fields):
        '''Crear y guardar usuarios'''
        if not email:
            raise ValueError('Los Usuarios deben tener un email')
        user = self.model(email=self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self,email,password):
        '''Crear súper usuario'''
        user = self.create_user(email,password)
        user.is_staff = True
        user.is_superuser= True
        user.save(using=self._db)

        return user
        
class User(AbstractBaseUser,PermissionsMixin):
    '''Modelo de usuario personalizado para aceptar el email en el login'''
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

class Residue(models.Model):
    '''Crear modelo de residuo'''
    img_src =models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,  
    )
    priority = models.IntegerField()
    date = models.DateField(auto_now_add=True,null=True)
    status = models.CharField(max_length=255)
    lat = models.CharField(max_length=255,default=0)
    lon = models.CharField(max_length=255,default=0)

