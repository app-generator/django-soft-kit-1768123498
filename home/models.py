# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    telefono = models.IntegerField(null=True, blank=True)
    imagen = models.CharField(max_length=255, null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    mensajes = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Sliders(models.Model):

    #__Sliders_FIELDS__
    nombre = models.CharField(max_length=255, null=True, blank=True)
    imagenes = models.TextField(max_length=255, null=True, blank=True)
    folder = models.CharField(max_length=255, null=True, blank=True)
    descripcion = models.TextField(max_length=255, null=True, blank=True)

    #__Sliders_FIELDS__END

    class Meta:
        verbose_name        = _("Sliders")
        verbose_name_plural = _("Sliders")


class Notas(models.Model):

    #__Notas_FIELDS__
    titulo = models.CharField(max_length=255, null=True, blank=True)
    contenido = models.TextField(max_length=255, null=True, blank=True)
    icono = models.CharField(max_length=255, null=True, blank=True)
    activo = models.BooleanField()

    #__Notas_FIELDS__END

    class Meta:
        verbose_name        = _("Notas")
        verbose_name_plural = _("Notas")


class Testimonio(models.Model):

    #__Testimonio_FIELDS__
    usuarios = models.CharField(max_length=255, null=True, blank=True)
    titulo = models.CharField(max_length=255, null=True, blank=True)
    contenido = models.TextField(max_length=255, null=True, blank=True)
    imagen = models.CharField(max_length=255, null=True, blank=True)

    #__Testimonio_FIELDS__END

    class Meta:
        verbose_name        = _("Testimonio")
        verbose_name_plural = _("Testimonio")


class Blog(models.Model):

    #__Blog_FIELDS__
    usuario = models.CharField(max_length=255, null=True, blank=True)
    contenido = models.TextField(max_length=255, null=True, blank=True)
    imagen = models.CharField(max_length=255, null=True, blank=True)
    respuesta = models.TextField(max_length=255, null=True, blank=True)

    #__Blog_FIELDS__END

    class Meta:
        verbose_name        = _("Blog")
        verbose_name_plural = _("Blog")



#__MODELS__END
