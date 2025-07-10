convert a temporal data in string format to datetime object.

```
>>> from datetime import datetime
>>> t = '2012-09-20'
>>> y = datetime.strptime(t, "%Y-%m-%d")
>>> z = datetime.now()
>>> z-y
datetime.timedelta(days=4676, seconds=38695, microseconds=648810)
```

convert a datetime object to string output.

```
>>> datetime.strftime(y, '%A %B %d, %Y')
'Thursday September 20, 2012'
>>> datetime.strftime(z, '%A %B %d, %Y')
'Thursday July 10, 2025'
>>> datetime.strftime(z, "%Y-%m-%d")
'2025-07-10'
```
