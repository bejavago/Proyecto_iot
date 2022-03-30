from django.db import models
from login_reg_app.models import User

class Device(models.Model):
    type =  models.CharField(max_length = 60)
    added_by = models.ForeignKey(User,related_name = 'uploaded_item', on_delete = models.CASCADE)
    placed = models.CharField(max_length = 60)
    details= models.CharField(max_length = 60)
    #temp = models.CharField(max_length = 60)
    #hum = models.CharField(max_length = 60)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


    