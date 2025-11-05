from django.db import models


class TestMetrics(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    coverage_percent = models.FloatField(null=True, blank=True)
    total_tests = models.IntegerField(null=True, blank=True)
    failures = models.IntegerField(null=True, blank=True)
    errors = models.IntegerField(null=True, blank=True)
    duration = models.FloatField(null=True, blank=True, help_text='Test run duration in seconds')
    report_path = models.CharField(max_length=512, blank=True)
    status = models.CharField(max_length=32, default='ok', help_text='ok/failed')

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"Metrics {self.created:%Y-%m-%d %H:%M} — {self.coverage_percent or 'N/A'}%"
