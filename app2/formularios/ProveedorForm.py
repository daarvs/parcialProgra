from django import forms
from app2.models import Proveedores

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedores
        fields = ('nombre', 'telefono')