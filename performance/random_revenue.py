"""
Problem:
Create a script called `random_revenue.py`. In this script filter the queryset using `filter_by_min_roi` previously created and save in a variable all the daily performance where the roi > 50%. Print the length of the queryset. Print the length of the queryset multiplied by 2. Expected query set length ~= 50.000 records. In a loop show the index of the loop out of the length of the queryset: 1/50000, 2/50000, 3/50000 and so on. In the same loop assign a new value to the revenue = revenue multiplied by a random factor which goes between 0.5 and 2 and save the daily_revenue with the new values
"""

import random
from datetime import datetime, timedelta

from .models import *


# Create a queryset with all the daily performance where the roi > 50%
queryset = DailyPerformance.objects.filter_by_min_roi(min_roi=0.5)
print(queryset.count())
print(queryset.count() * 2)

# In a loop show the index of the loop out of the length of the queryset
# 1/50000, 2/50000, 3/50000 and so on
for index, daily_performance in enumerate(queryset):
    print(f'{index + 1}/{queryset.count()}')

# In the same loop assign a new value to the revenue = revenue multiplied
# by a random factor which goes between 0.5 and 2 and save the daily_revenue
# with the new values
for daily_performance in queryset:
    daily_performance.revenue = daily_performance.revenue * \
        random.uniform(0.5, 2)
    daily_performance.save()
