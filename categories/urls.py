from django.urls import path
from . import views

app_name = 'categories'

urlpatterns = [
    # Define your URL patterns here
]


urlpatterns += [
    path('', views.category_list, name='category_list'),
    path('<slug:slug>/', views.category_detail, name='category_detail'),
    path('create/', views.category_create, name='category_create'),
    path('update/<slug:slug>/', views.category_update, name='category_update'),
    path('delete/<slug:slug>/', views.category_delete, name='category_delete'),
]

