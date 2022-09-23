"""
Problem:
Create another script called `slow_iteration.py`. In this script get a DailyPerformance queryset limiting it to 50 records. Iter over this queryset, and add a `time.sleep(60)` inside the loop. Implement this with celery task.
"""

from celery import Celery
import time

from .models import DailyPerformance

# Get a DailyPerformance queryset limiting it to 50 records
queryset = DailyPerformance.objects.all()[:50]


"""
# Iter over this queryset, and add a `time.sleep(60)` inside the loop
for daily_performance in queryset:
    time.sleep(60)
"""

# Implement this with celery task

app = Celery('tasks', broker='redis://localhost:6379/0')


@app.task
def slow_iteration():
    queryset = DailyPerformance.objects.all()[:50]
    for daily_performance in queryset:
        time.sleep(60)


# Run the task
slow_iteration.delay()
