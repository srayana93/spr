from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, UserProfile, VendorProfile, Address

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_vendor')

    def save(self, commit=True):
        user = super().save(commit=False)
        if user.is_vendor:
            user.is_staff = True  # Vendors are considered staff in this context
            user.is_customer = False
        if commit:
            user.save()
        return user

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'date_of_birth', 'is_vendor', 'is_staff')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['date_of_birth', 'profile_picture']

class VendorProfileForm(forms.ModelForm):
    class Meta:
        model = VendorProfile
        fields = ['company_name', 'company_website', 'business_address', 'business_phone']

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['name', 'mobile', 'address1', 'address2', 'city', 'state', 'pincode', 'country']