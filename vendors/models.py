from django.db import models
from accounts.models import CustomUser

class VendorProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='vendor_profile')
    company_name = models.CharField(max_length=255)
    company_website = models.URLField(max_length=200, blank=True)
    business_address = models.CharField(max_length=255, blank=True)
    business_phone = models.CharField(max_length=15, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name