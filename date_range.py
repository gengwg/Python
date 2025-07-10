from datetime import datetime, date, timedelta
import calendar

# Function to get the first and last day of the month
# If no start_date is provided, it defaults to the first day of the current month
def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date.replace(day=days_in_month)
    return start_date, end_date

# Example usage of get_month_range
print("------------ Month Range -----------")
a_day = timedelta(days=1)
first_day, last_day = get_month_range()
print(f"First day: {first_day}, Last day: {last_day}")

# Print each day in the month range
print("\n------------ Days in Month -----------")
while first_day <= last_day:
    print(first_day)
    first_day += a_day

# Function to generate a date range
# from start to stop with a specified step
# Default step is one day
def date_range(start, stop, step=a_day):
    while start < stop:
        yield start
        start += step

# Example usage of date_range
print("\n------------ Date Range -----------")

first_day, last_day = get_month_range()
for d in date_range(first_day, last_day):
    print(d)

for d in date_range(datetime(2012, 9, 1), datetime(2012, 9, 5), timedelta(hours=6)):
    print(d)