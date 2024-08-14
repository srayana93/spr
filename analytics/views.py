from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import *
from .forms import *

# Replace the code in each app below with specific logic as per the app's requirements

@login_required
def analytics_dashboard(request):
    order_data = request.user.order_analytics.all()
    product_views = request.user.product_views.all()
    return render(request, 'analytics/analytics_dashboard.html', {'order_data': order_data, 'product_views': product_views})

@login_required
def report_list(request):
    reports = request.user.order_analytics.all()
    return render(request, 'analytics/report_list.html', {'reports': reports})

@login_required
def report_detail(request, report_id):
    report = get_object_or_404(OrderAnalytics, id=report_id)
    return render(request, 'analytics/report_detail.html', {'report': report})

@login_required
def report_generate(request):
    # Implement report generation logic here
    return render(request, 'analytics/report_generate.html')

