from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

from .models import TestMetrics


@staff_member_required
def dashboard(request):
    # show last 20 metrics for charts
    metrics = TestMetrics.objects.all()[:20][::-1]
    return render(request, 'metrics/dashboard.html', {'metrics': metrics})
