from django.db import models
from login_reg_app.models import User


class Device(models.Model):
    
    TYPE_DEVICE = (
        ('Arduino UNO', 'Arduino UNO'),
        ('Raspberry', 'Raspberry'),  # ESPECIFICAR TIPOS DE DEVICES
        ('ESP8266', 'ESP8266'),
        ('ESP32', 'ESP32'),
        # CAMPO PARA AGREGAR MAS DEVICES
    )
    
    COUNTRY_CHOICES = (
        ('Colombia', 'Colombia'),
        ('Argentina', 'Argentina'),
        ('Brasil', 'Brasil'),
        ('Chile', 'Chile'),
    )
    
    
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=TYPE_DEVICE)
    device_id = models.CharField(max_length=255, blank=True)
    placed = models.CharField(max_length=20, choices=COUNTRY_CHOICES)
    details= models.CharField(max_length = 60, blank=True)
    imageDevice = models.FileField(upload_to='images/', blank=True)
    added_by = models.ForeignKey(User,related_name = 'uploaded_item', on_delete = models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.name + ' - ' + self.type + ' - ' + self.placed 


