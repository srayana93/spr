
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("products/", include("products.urls")),
    path("categories/", include("categories.urls")),
    path("cart/", include("cart.urls")),
    path("orders/", include("orders.urls")),
    path("wishlist/", include("wishlist.urls")),
    path("payments/", include("payments.urls")),
    path("analytics/", include("analytics.urls")),
    path("vendors/", include("vendors.urls")),
    path("chat/", include("chat.urls")),
]
