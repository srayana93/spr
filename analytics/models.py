from django.db import models
from accounts.models import CustomUser
from products.models import Product

class ProductView(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, related_name='product_views')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='views')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email if self.user else 'Anonymous'} viewed {self.product.name}"

class OrderAnalytics(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='order_analytics')
    total_orders = models.PositiveIntegerField(default=0)
    total_spent = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    last_order_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Order Analytics for {self.user.email}"