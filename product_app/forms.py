from django import forms
from django import views
from .models import *



class StockInputForm(forms.Form):
    quantity = forms.CharField(label="Quantity", widget=forms.TextInput(attrs={'placeholder': 'Product Quantity'}))
    location = forms.ModelChoiceField(queryset=Location.objects.all())
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    operation_type = forms.CharField(label="Operation Type", widget=forms.Select(choices=OPERATION_TYPE))



# class StockOutputForm(forms.Form):
#     quantity = forms.CharField(label="Quantity", widget=forms.TextInput(attrs={'placeholder': 'Product Quantity'}))
#     from_location = forms.CharField(label="From Location",widget=forms.TextInput(attrs={'placeholder': 'From Location'}))
#     to_location = forms.CharField(label="To Location", widget=forms.TextInput(attrs={'placeholder': 'To Location'}))
