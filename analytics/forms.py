from django import forms
from .models import OrderAnalytics

class OrderAnalyticsForm(forms.ModelForm):
    class Meta:
        model = OrderAnalytics
        fields = ['total_orders', 'total_spent', 'last_order_date']