from datetime import datetime, timedelta
from pytz import timezone

# Get the current datetime
d = datetime.now()
print(d)

# Localize the datetime to a specific timezone
west = timezone('America/Los_Angeles')
d_west = west.localize(d)
print(d_west)

# Convert to another timezone
china = timezone('Asia/Shanghai')
d_china = d_west.astimezone(china)
print(d_china)

# If you perform arithmetic with localized datetimes, you should normalize them to handle Daylight Saving Time (DST) correctly.
d = datetime(2013, 3, 10, 1, 45)
west = timezone('America/Los_Angeles')
d_west = west.localize(d)
print(d_west)

# Attempt to add an hour to localized dates without normalization may lead to incorrect time due to DST.
later_wrong = d_west + timedelta(hours=1)
print(later_wrong)

# Normalize the datetime to handle DST correctly
later = west.normalize(d_west + timedelta(hours=1))
# later = west.normalize(later_wrong)
print(later)