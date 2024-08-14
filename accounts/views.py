from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import *
from .forms import *

# Replace the code in each app below with specific logic as per the app's requirements

@login_required
def profile_view(request):
    user = request.user
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('accounts:profile')
    else:
        profile_form = UserProfileForm(instance=user.profile)
    return render(request, 'accounts/profile.html', {'profile_form': profile_form})

