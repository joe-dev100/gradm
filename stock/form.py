from django import forms
from .models import Entree, EntreeItems, SortieStock, SortieItems


class EntreeForm(forms.ModelForm):
    class Meta:
        model = Entree
        fields = '__all__'
        
class EntreeItemsForm(forms.ModelForm):
    class Meta:
        model = EntreeItems
        fields = ['product', 'qty']