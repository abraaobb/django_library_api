from django.contrib import admin
from .models import TestMetrics
from django.utils.html import format_html


@admin.register(TestMetrics)
class TestMetricsAdmin(admin.ModelAdmin):
    list_display = ('created', 'coverage_percent', 'total_tests', 'failures', 'errors', 'status', 'dashboard_link')
    readonly_fields = ('created',)
    list_filter = ('status',)
    search_fields = ('report_path',)

    def dashboard_link(self, obj):
        return format_html('<a href="/metrics/" target="_blank">Open dashboard</a>')

    dashboard_link.short_description = 'Dashboard'
