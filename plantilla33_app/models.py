from django.db import models
from login_reg_app.models import User


class Device(models.Model):
    
    TYPE_DEVICE = (
        ('A', 'OPCION A'),  # ESPECIFICAR TIPOS DE DEVICES
        ('B', 'OPCION B'),
        ('C', 'OPCION C'),
        ('D', 'OPCION D'),
    )
    
    COUNTRY_CHOICES = (
        ('Colombia', 'Colombia'),
        ('Argentina', 'Argentina'),
        ('Brasil', 'Brasil'),
        ('Chile', 'Chile'),
    )
        
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=1, choices=TYPE_DEVICE)
    placed = models.CharField(max_length=20, choices=COUNTRY_CHOICES)
    details= models.CharField(max_length = 60, blank=True)
    added_by = models.ForeignKey(User,related_name = 'uploaded_item', on_delete = models.CASCADE)
    #temp = models.CharField(max_length = 60)
    #hum = models.CharField(max_length = 60)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.name + ' - ' + self.type + ' - ' + self.placed 


