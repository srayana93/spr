from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # Define your URL patterns here
]


urlpatterns += [
    path('profile/', views.profile_view, name='profile'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('password_reset/', views.password_reset_view, name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/', views.password_reset_confirm_view, name='password_reset_confirm'),
]

