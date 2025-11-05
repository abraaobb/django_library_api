import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

from django.core.management.base import BaseCommand

from metrics.models import TestMetrics


class Command(BaseCommand):
    help = 'Run tests with coverage and collect basic metrics into TestMetrics model.'

    def handle(self, *args, **options):
        base = Path.cwd()
        cov_file = base / 'coverage.xml'

        # Run tests under coverage
        self.stdout.write('Running tests under coverage...')
        try:
            # Run coverage + Django tests using the current Python interpreter to call coverage as a module
            run = subprocess.run(
                [sys.executable, '-m', 'coverage', 'run', '--source=.', 'manage.py', 'test'],
                cwd=base,
                capture_output=True,
                text=True,
                check=False,
            )
        except FileNotFoundError:
            self.stderr.write('coverage is not installed. Please install it (pip install coverage).')
            return

        stdout = run.stdout + '\n' + run.stderr

        # Generate coverage xml
        subprocess.run([sys.executable, '-m', 'coverage', 'xml', '-o', str(cov_file)], cwd=base)

        coverage_percent = None
        total_tests = None
        failures = None
        errors = None
        duration = None

        # Parse coverage.xml basic metric
        if cov_file.exists():
            try:
                tree = ET.parse(str(cov_file))
                root = tree.getroot()
                # coverage.py XML has tags like <coverage line-rate="0.97" ...>
                line_rate = root.attrib.get('line-rate') or root.attrib.get('lines-valid')
                if line_rate:
                    # if line-rate is a float between 0 and 1
                    try:
                        lr = float(root.attrib.get('line-rate', 0))
                        coverage_percent = round(lr * 100, 2)
                    except Exception:
                        coverage_percent = None
            except ET.ParseError:
                self.stderr.write('Failed to parse coverage.xml')

        # Try to extract test counts from stdout: 'Ran X tests in 0.00s'
        m = re.search(r'Ran (\d+) tests? in ([0-9\.]+)s', stdout)
        if m:
            total_tests = int(m.group(1))
            try:
                duration = float(m.group(2))
            except Exception:
                duration = None

        # Try to detect failures/errors summary
        # Django prints something like 'FAILED (failures=1, errors=0)'
        m2 = re.search(r'FAILED \((.*?)\)', stdout)
        if m2:
            details = m2.group(1)
            fd = re.search(r'failures=(\d+)', details)
            ed = re.search(r'errors=(\d+)', details)
            failures = int(fd.group(1)) if fd else 0
            errors = int(ed.group(1)) if ed else 0
        else:
            # assume zero if no FAILED line
            failures = 0
            errors = 0

        # Save to DB
        tm = TestMetrics.objects.create(
            coverage_percent=coverage_percent,
            total_tests=total_tests,
            failures=failures,
            errors=errors,
            duration=duration,
            report_path=str(cov_file) if cov_file.exists() else '',
            status='failed' if (failures or errors) else 'ok',
        )

        self.stdout.write(self.style.SUCCESS(f'Created TestMetrics id={tm.id} coverage={coverage_percent}% tests={total_tests}'))
