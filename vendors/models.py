from django.db import models
from accounts.models import CustomUser

class VendorProfile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='vendors_vendor_profile'  # Change this related name
    )

    def __str__(self):
        return self.company_name