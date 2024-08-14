from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView, PasswordChangeView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomUserChangeForm, AddressForm, UserProfileForm
from .models import UserProfile, Address

def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("home")

@login_required
def profile_view(request):
    user_profile = getattr(request.user, 'profile', None)
    address = Address.objects.filter(user=request.user).first()
    
    if request.method == "POST":
        profile_form = CustomUserChangeForm(request.POST, instance=request.user)
        address_form = AddressForm(request.POST, instance=address)
        picture_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

        if profile_form.is_valid() and address_form.is_valid() and picture_form.is_valid():
            profile_form.save()
            address_form.save()
            picture_form.save()
            return redirect("profile")
    else:
        profile_form = CustomUserChangeForm(instance=request.user)
        address_form = AddressForm(instance=address)
        picture_form = UserProfileForm(instance=user_profile)

    context = {
        "profile_form": profile_form,
        "address_form": address_form,
        "picture_form": picture_form,
    }
    return render(request, "accounts/profile.html", context)

@login_required
def edit_profile_view(request):
    user_profile = getattr(request.user, 'profile', None)
    address = Address.objects.filter(user=request.user).first()
    
    if request.method == "POST":
        profile_form = CustomUserChangeForm(request.POST, instance=request.user)
        address_form = AddressForm(request.POST, instance=address)
        picture_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

        if profile_form.is_valid() and address_form.is_valid() and picture_form.is_valid():
            profile_form.save()
            address_form.save()
            picture_form.save()
            return redirect("profile")
    else:
        profile_form = CustomUserChangeForm(instance=request.user)
        address_form = AddressForm(instance=address)
        picture_form = UserProfileForm(instance=user_profile)

    context = {
        "profile_form": profile_form,
        "address_form": address_form,
        "picture_form": picture_form,
    }
    return render(request, "accounts/edit_profile.html", context)

class CustomPasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset.html'
    form_class = PasswordResetForm
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/password_change.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_change_done')
