from datetime import datetime, timedelta

from django import forms
from django.utils import timezone

from .models import Order, BouquetType


class FlowerOrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['name', 'phone_no', 'description', 'size', 'quantity', 'bouquet_type', 'shipping_address',]
        labels = {'name': 'First Name', 'phone_no': 'Contact phone number', 'description': 'Feel free to give us a short description:', 'quantity': 'Quantity', 'bouquet_type': 'Bouquet Type'}
        widgets = {'description': forms.Textarea}



# class FlowerForm(forms.Form):
#     name = forms.CharField(label='Name', max_length=100)
#     description = forms.CharField(label='Description', max_length=100)
#     size = forms.ChoiceField(label='Size', choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')])
#     amount = forms.IntegerField(label='How many?')
#     type = forms.ChoiceField(label='Bouquet Type', choices=[('Nosegay Bouquet', 'Nosegay Bouquet')])


class MultipleOrderForm(forms.Form):
    number = forms.IntegerField(min_value=3, max_value=20)


