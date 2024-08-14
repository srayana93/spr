from django import forms
from accounts.models import Address

class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['name', 'mobile', 'address1', 'address2', 'city', 'state', 'pincode', 'country']