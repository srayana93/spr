from django import forms
from .models import WishListItem

class AddToWishListForm(forms.ModelForm):
    class Meta:
        model = WishListItem
        fields = ['product']

class RemoveFromWishListForm(forms.ModelForm):
    class Meta:
        model = WishListItem
        fields = []