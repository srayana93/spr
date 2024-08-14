from django.urls import path
from . import views

app_name = 'analytics'

urlpatterns = [
    # Define your URL patterns here
]


urlpatterns += [
    path('dashboard/', views.analytics_dashboard, name='dashboard'),
    path('reports/', views.report_list, name='report_list'),
    path('report/<int:report_id>/', views.report_detail, name='report_detail'),
    path('report/generate/', views.report_generate, name='report_generate'),
]

