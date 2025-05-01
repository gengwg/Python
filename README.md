# Python
Python Cookbooks and Examples


## Creating virtual environments

### Install venv

On Ubuntu/Debian:

```
apt-get install python3-venv
```

On CentOS 7, it's already installed together with the python3 package.

### Create virtual environments

```bash
# create virtual env
python3 -m venv myvenv
# or equivalent
pyvenv myvenv

# activate virtual env
pi@host:~$ source myvenv/bin/activate
(myvenv) pi@host:~$

# upgrade pip3
(myvenv) user@host:~$ pip3 --version
pip 9.0.1 from /home/pi/myvenv/lib/python3.5/site-packages (python 3.5)
(myvenv) user@host:~$ python3 -m pip install --upgrade pip
(myvenv) user@host:~$ python3 -m pip --version
pip 20.2.2 from /home/pi/myvenv/lib/python3.5/site-packages/pip (python 3.5)

# install package example
(myvenv) pi@host:~$ python3 -m pip install requests
# or equivalent
(myvenv) user@host:~$ pip3 install requests

# test import installed package
(myvenv) pi@host:~$ python3 -c 'import requests'

# deactivate virtual env
(myvenv) pi@host:~$ deactivate
pi@host:~$
```

## Notes

The trailing comma has no special meaning in a list or dictionary, but can be useful when using source code change management tools.

The trailing comma can be helpful in minimising how many lines changed when adding new lines; adding an additional line to a dictionary with a trailing comma would not change the last existing entry:

```python
a_value = {
    key1: value1,
    key2: value2,
    # inserting here doesn't require adding a comma
    # to the preceding line.
}
```

### Start a simple HTTP server

```
# Python 2.7
python -m SimpleHTTPServer 7777

# Python 3
python -m http.server 7777
```

### pip install requirements.txt

```
python3 -m pip install -r requirements.txt
```

### Always get short hostname

`socket.gethostname()` on some hosts get FQDN, on others it gets short hostname. To only get short host name:

```
import socket
socket.gethostname().split('.', 1)[0]
```

### Format string using named parameters

```
import socket

sql = 'INSERT INTO table (hostname, ip4addr, label, ip6addr) VALUES ("{hostname}", "{ip4addr}", "infra", "{ip6addr}");'

with open("hosts.txt") as f:
    for line in f:
        host = line.strip()
        ip4 = socket.gethostbyname(host)
        ip6 = socket.getaddrinfo(host, None, socket.AF_INET6)[0][4][0]
        print(sql.format(hostname=host, ip4addr=ip4, ip6addr=ip6))
```

### Safe max() for empty lists

```
>>> max([], default=0)
0
```

### Insert to beginning of list

```
>>> array = [1, 2, 3, 4]
>>> array.insert(0, 5)
>>> array
[5, 1, 2, 3, 4]
```

### Sort Dictionary by Value in Descending Order

```
orders = {"cappuccino": 54, "latte": 56, "espresso": 72, "americano": 48, "cortado": 41}

print({k: v for k, v in sorted(orders.items(), key=lambda x: x[1], reverse=True)})
# [print(k, v) for k, v in sorted(orders.items(), key=lambda x: x[1], reverse=True)]

```

### Print ASCII non-printable characters

```
>>> print(b'hi\n'.decode('ascii'))
hi

>>> print(b'hi\n')
b'hi\n'
```

### Print gibberish unicode characters

```
>>> print(u"\u5DDD\u666E\u88AB\u63A8\u7279\u6C38\u4E45\u5C01\u53F7")
川普被推特永久封号
```

### Split text after the second occurrence of character

```
>>> a = "some-sample-filename-to-split"
>>> "-".join(a.split("-", 2)[:2])
'some-sample'
>>> a.split("-", 2)[2]
'filename-to-split'
```

### f-strings

Python f-strings are available since Python 3.6. The string has the f prefix and uses {} to evaluate variables.

```python
name = 'Peter'
age = 23

print('%s is %d years old' % (name, age))
print('{} is {} years old'.format(name, age))
print(f'{name} is {age} years old')


bags = 3
apples_in_bag = 12

print(f'There are total of {bags * apples_in_bag} apples')
# There are total of 36 apples

# format_datetime.py

import datetime

now = datetime.datetime.now()

print(f'{now:%Y-%m-%d %H:%M}')
# 2021-01-12 12:31

print(f'{now:%B %d, %Y}')
# January 12, 2021
```

### List members of a Unix group name

```py
import grp
print(grp.getgrnam('docker').gr_mem)
# ['username1']
```

### Datetime

datetime.datetime.now() takes tzinfo as keyword argument but datetime.today() does not take any keyword arguments.

By default, now() executes with datetime.datetime.now(tz=None)

```python
>>> import pytz
>>> datetime.datetime.now(tz=pytz.timezone('US/Eastern'))
datetime.datetime(2021, 1, 12, 15, 33, 5, 893121, tzinfo=<DstTzInfo 'US/Eastern' EST-1 day, 19:00:00 STD>)
>>> datetime.datetime.today(tz=pytz.timezone('US/Eastern'))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: today() takes no keyword arguments
```

### Get IPv6 address

This follows nsswitch.conf, e.g. search `/etc/hosts` first.

```
>>> import socket
>>> socket.getaddrinfo('google.com', None, socket.AF_INET6)
[(<AddressFamily.AF_INET6: 10>, <SocketKind.SOCK_STREAM: 1>, 6, '', ('2401:db00:25ff:c83::', 0, 0, 0)), (<AddressFamily.AF_INET6: 10>, <SocketKind.SOCK_DGRAM: 2>, 17, '', ('2401:db00:25ff:c83::', 0, 0, 0)), (<AddressFamily.AF_INET6: 10>, <SocketKind.SOCK_RAW: 3>, 0, '', ('2401:db00:25ff:c83::', 0, 0, 0))]

# Real DNS IP
$ dig AAAA google.com +short
2607:f8b0:400a:80a::200e
```

### sort a dictionary by value

```
>>> x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
>>> sorted(x.items(), key=lambda z: z[1])
[(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
>>> [(k,v) for k,v in sorted(x.items(), key=lambda z: z[1])]
[(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
# get keys only
>>> [k for k,v in sorted(x.items(), key=lambda z: z[1])]
[0, 2, 1, 4, 3]
```

### Install pip module

```
$ python3 -m pip install --user pygame
/usr/bin/python3: No module named pip
```

===>

```
$ sudo apt install python3-pip
```

```
$ python3 -m pip install --user pygame
error: externally-managed-environment
```

Thiss error occurs because newer versions of Python on Debian/Ubuntu systems block user/global pip installations by default (PEP 668) to prevent conflicts with system packages. Here's how to  resolve it:

```
sudo apt install python3-pygame
```

## Errors

### mysql.connector error

```
ImportError: No module named mysql.connector
```

===>

```
python3 -m pip install mysql-connector-python
```

```
>>> time.struct_time(tm_year=2020, tm_mon=10, tm_mday=9, tm_hour=0, tm_min=28, tm_sec=35, tm_wday=4, tm_yday=283, tm_isdst=-1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: structseq() takes at most 2 arguments (9 given)
```

===>

```
>>> dict(tm_year=2020, tm_mon=10, tm_mday=9, tm_hour=0, tm_min=28, tm_sec=35, tm_wday=4, tm_yday=283, tm_isdst=-1).values()
dict_values([2020, 10, 9, 0, 28, 35, 4, 283, -1])
>>> time.struct_time(dict(tm_year=2020, tm_mon=10, tm_mday=9, tm_hour=0, tm_min=28, tm_sec=35, tm_wday=4, tm_yday=283, tm_isdst=-1).values())
time.struct_time(tm_year=2020, tm_mon=10, tm_mday=9, tm_hour=0, tm_min=28, tm_sec=35, tm_wday=4, tm_yday=283, tm_isdst=-1)
```
