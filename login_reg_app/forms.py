from django import forms
from login_reg_app.models import User
from login_reg_app.views import *


class RegisterForm(forms.ModelForm):
    
    class Meta:
        model = User    #Usuario es la clase creada en la BD
        fields = ['nombre', 'username', 'email', 'password']
        
        labels = {
            'nombre': 'Nombre:  ',
            'username': 'Username:  ',
            'email': 'Correo  ',  
            'password': 'Contraseña  ',
        }
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}), 
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),  
        }

class LoginForm(forms.ModelForm):
    
    class Meta:
        model = User    #Usuario es la clase creada en la BD
        fields = ['username', 'password']
                
        labels = {
            'username': 'User/Correo:  ',
            'password': 'Contraseña  ',
        }    
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}), 
            'password': forms.PasswordInput(attrs={'class': 'form-control'}), 
        }
        
        
             
        
 