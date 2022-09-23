from django.db import models

"""
Problem: 
Write a model called Performance which has cost, revenue and creation date. Add a new field for profit, which is the spread between revenue and costs. Extend this class with two other classes HourlyPerformance, DailyPerformance. HourlyPerformance has to have a datetime field called datetime. DailyPerformance has to have a date field called date. Please note, any migration hasn’t been performed yet and the model Performance doesn't need to be in the db. Create a method called filter_by_min_roi(min_roi: float)  so you can do DailyPerformance.objects.filter_by_min_roi(min_roi=0.5)
"""


class Performance(models.Model):
    cost = models.FloatField()
    revenue = models.FloatField()
    creation_date = models.DateTimeField(auto_now_add=True)

    @property
    def profit(self):
        return self.revenue - self.cost


class HourlyPerformance(Performance):
    datetime = models.DateTimeField()


class DailyPerformance(Performance):
    date = models.DateField()

    @classmethod
    def filter_by_min_roi(cls, min_roi):
        return cls.objects.filter(
            revenue__gt=models.F('cost') * min_roi
        )
