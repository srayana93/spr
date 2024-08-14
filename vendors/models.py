from django.db import models
from accounts.models import CustomUser  # Import CustomUser from accounts

class VendorProfile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='vendor_profile_vendors'  # Ensure unique related_name
    )
    company_name = models.CharField(null=True, blank=True)
    business_address = models.CharField(null=True, blank=True)
    business_phone = models.CharField(max_length=15)
    company_website = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name
