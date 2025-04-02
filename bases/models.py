from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django_userforeignkey.models.fields import UserForeignKey


class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)
    fc = models.DateTimeField(auto_now_add=True)
    fm = models.DateTimeField(auto_now=True)
    uc = models.ForeignKey(User, on_delete=models.CASCADE)
    um = models.IntegerField(blank=True,null=True)

    class Meta:
        abstract=True


class ClaseModelo2(models.Model):
    estado = models.BooleanField(default=True)
    fc = models.DateTimeField(auto_now_add=True)
    fm = models.DateTimeField(auto_now=True)
    # user = UserForeignKey(auto_user_add=True, verbose_name="El usuario es asignado automaticamente", related_name="parametro")
    uc = UserForeignKey(auto_user_add=True,verbose_name="El usuario creacion es asignado automaticamente",related_name='+')
    um = UserForeignKey(auto_user=True,verbose_name="El usuario modificador es asignado automaticamente",related_name='+')

    class Meta:
        abstract=True
        

# class Rol(models.Model):    
#     nombre = models.CharField(max_length=100)
#     estado = models.BooleanField(default=True)
    
# class User(AbstractUser):
#     rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True)