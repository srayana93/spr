from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import *
from .forms import *

# Replace the code in each app below with specific logic as per the app's requirements

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/categories_list.html', {'categories': categories})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'categories/categories_detail.html', {'category': category})

@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('categories:category_list')
    else:
        form = CategoryForm()
    return render(request, 'categories/categories_create.html', {'form': form})

@login_required
def category_update(request, slug):
    category = get_object_or_404(Category, slug=slug)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories:category_detail', slug=slug)
    else:
        form = CategoryForm(instance=category)
    return render(request, 'categories/categories_update.html', {'form': form})

@login_required
def category_delete(request, slug):
    category = get_object_or_404(Category, slug=slug)
    if request.method == 'POST':
        category.delete()
        return redirect('categories:category_list')
    return render(request, 'categories/categories_delete.html', {'category': category})

