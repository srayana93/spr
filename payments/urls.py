from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    # Define your URL patterns here
]


urlpatterns += [
    path('form/', views.payment_form, name='payment_form'),
    path('success/', views.payment_success, name='payment_success'),
    path('failure/', views.payment_failure, name='payment_failure'),
]

