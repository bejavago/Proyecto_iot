from django import forms

from .models import Device

class DeviceForm(forms.ModelForm):
    
    # VALIDACIONES
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) > 8:
            raise forms.ValidationError('El nombre no puede tener mas de 8 caracteres')
        return name
    
    def clean_type(self):
        type = self.cleaned_data.get('type')
        if type == '':
            raise forms.ValidationError('Debe elegir un tipo de dispositivo')
        return type
    
    def clean_placed(self):
        placed = self.cleaned_data.get('placed')
        if placed == '':
            raise forms.ValidationError('Debe elegir un lugar')
        return placed
    
    
    class Meta:
        model = Device
        fields = ['name','type', 'placed', 'details']
        
        labels = {
            'name': 'Device Name',
            'type': 'Device Type',
            'placed': 'Placed',
            'details': 'Details',
        }
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-select'}),
            'placed': forms.Select(attrs={'class': 'form-select'}),
            'details': forms.Textarea(attrs={'class': 'form-control', 'rows': '2'}),
        }
        

        
