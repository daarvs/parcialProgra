from django import forms
from app2.models import Sucursal

class SucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        fields = ('nombre', 'localizacion')