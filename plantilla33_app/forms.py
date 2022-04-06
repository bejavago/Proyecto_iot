from django import forms

from .models import Device

class DeviceForm(forms.ModelForm):
    
    # VALIDACIONES
    

    
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
        fields = ['name','device_id','type', 'placed', 'details', 'imageDevice']
        
        labels = {
            'name': 'Device Name',
            'device_id': 'Device ID',
            'type': 'Device Type',
            'placed': 'Placed',
            'details': 'Details',
            'imageDevice': 'Image',
        }
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'device_id': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-select'}),
            'placed': forms.Select(attrs={'class': 'form-select'}),
            'details': forms.Textarea(attrs={'class': 'form-control', 'rows': '2'}),
        }
        

        
