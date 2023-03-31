# forms.py

from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nome', 'cognome', 'codice_fiscale', 'stato', 'nome_instagram']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cognome': forms.TextInput(attrs={'class': 'form-control'}),
            'codice_fiscale': forms.TextInput(attrs={'class': 'form-control'}),
            'stato': forms.Select(attrs={'class': 'form-control'}),
            'nome_instagram': forms.TextInput(attrs={'class': 'form-control'}),
        }
