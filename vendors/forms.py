from django import forms
from .models import VendorProfile

class VendorProfileForm(forms.ModelForm):
    class Meta:
        model = VendorProfile
        fields = ['company_name', 'company_website', 'business_address', 'business_phone']