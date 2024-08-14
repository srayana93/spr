from django import forms
from .models import CartItem

class AddToCartForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['product', 'quantity']

class UpdateCartForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['quantity']

class CheckoutForm(forms.Form):
    address = forms.CharField(max_length=255)
    city = forms.CharField(max_length=50)
    state = forms.CharField(max_length=50)
    country = forms.CharField(max_length=50)
    postal_code = forms.CharField(max_length=20)