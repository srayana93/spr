from django.shortcuts import render
from categories.models import Category

def home_view(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})
