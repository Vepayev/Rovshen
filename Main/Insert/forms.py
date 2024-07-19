from django import forms
from .models import Insert

class InsertForm(forms.ModelForm):
    class Meta:
        model = Insert
        fields = ['senesi', 'gelen_tyr', 'gelen_haryt', 'acylan_tyr', 'cykan_haryt', 'cykman_duran_haryt', 'deklerant_algy', 'bellik']
        widgets = {
            'senesi': forms.DateInput(attrs={'type': 'date'}),
        }
