from django import forms
from django.forms.widgets import Select, TextInput

from .models import Stock, StockOperation, Location, Product


class StockForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)
    location = forms.ModelChoiceField(queryset=Location.objects.all())
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    operation_type = forms.ChoiceField(
        choices=(
            ('stock_input', 'Stock Input'), ('stock_output', 'Stock Output')
        )
    )


class StockOperationForm(forms.ModelForm):
    class Meta:
        model = StockOperation
        fields = ['quantity', 'location', 'product', 'operation_type']
        # widget = {
        #     'quantity': TextInput(
        #         attrs={'class': 'required form-control col-md-7 col-xs-12', 'placeholder': 'Quantity'}),
        #     'operation_type': Select(
        #         attrs={'class': 'required form-control col-md-7 col-xs-12', 'placeholder': 'Operation Type'}),
        #     'location': Select(
        #         attrs={'class': 'required form-control col-md-7 col-xs-12', 'placeholder': 'Location'}),
        #     'product': Select(
        #         attrs={'class': 'required form-control col-md-7 col-xs-12', 'placeholder': 'Product'}),
        #
        # }
