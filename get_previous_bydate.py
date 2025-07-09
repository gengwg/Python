from datetime import datetime, timedelta

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def get_previous_weekday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
        
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    
    # print(day_num, day_num_target)

    days_ago = (7 + day_num - day_num_target) % 7
    # If today is the target weekday, we want to go back 7 days
    # to get the previous occurrence.
    # This is different from dateutil's behavior, which returns today.
    if days_ago == 0:
        days_ago = 7
    previous_weekday = start_date - timedelta(days=days_ago)
    return previous_weekday

print(get_previous_weekday('Monday'))
print(get_previous_weekday('Friday'))
print(get_previous_weekday('Wednesday'))

### Using dateutil

from dateutil.relativedelta import relativedelta
from dateutil.rrule import *

d = datetime.now()
print(d + relativedelta(weekday=FR))  # Next Friday
print(d + relativedelta(weekday=FR(-1)))  # Last Friday
print(d + relativedelta(weekday=WE(-1)))  # Last Wednesday