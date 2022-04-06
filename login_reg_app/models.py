from __future__ import unicode_literals
from django.db import models



class User(models.Model):
    nombre = models.CharField(max_length=45, unique=True, verbose_name="Nombre", default=None)
    username = models.CharField(max_length=45, unique=True, verbose_name="Username", default=None)
    email = models.CharField(max_length=200, unique=True, verbose_name="Email", default=None)
    password = models.CharField(max_length=72, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects = UserManager()

    def __repr__(self):
        return f"User ID: {self.id}| nombre: {self.nombre}| Last Name: {self.username}| Email: {self.email}| Password: {self.password} ||"