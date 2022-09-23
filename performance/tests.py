from django.test import TestCase
from django.utils import timezone

from .models import DailyPerformance, HourlyPerformance, Performance


class PerformanceTestCase(TestCase):
    def setUp(self):
        self.performance = Performance.objects.create(
            cost=10,
            revenue=20,
            creation_date=timezone.now(),
        )

    def test_profit(self):
        profit = self.performance.profit
        self.assertEqual(profit, 10)


class HourlyPerformanceTestCase(TestCase):
    def setUp(self):
        self.hourly_performance = HourlyPerformance.objects.create(
            cost=10,
            revenue=20,
            datetime=timezone.now(),
        )

    def test_profit(self):
        self.assertEqual(self.hourly_performance.profit, 10)


class DailyPerformanceTestCase(TestCase):
    def setUp(self):
        self.daily_performance = DailyPerformance.objects.create(
            cost=10,
            revenue=20,
            date=timezone.now(),
        )

    def test_profit(self):
        self.assertEqual(self.daily_performance.profit, 10)

    def test_filter_by_min_roi(self):
        self.assertEqual(
            DailyPerformance.filter_by_min_roi(0.5).count(),
            1,
        )
