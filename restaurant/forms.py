from django import forms
from .models import MenuItem,Order, BlogPost

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['category','name', 'price', 'description', 'image', ]
        

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'customer_email', 'customer_phone', 'customer_address', 'quantity']
       
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'image', 'author', 'category']