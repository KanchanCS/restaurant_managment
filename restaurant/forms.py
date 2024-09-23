from django import forms
from .models import MenuItem,Order

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['category','name', 'price', 'description', 'image', ]
        

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'customer_email', 'customer_phone', 'customer_address', 'quantity']
       
