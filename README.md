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

### Safe max() for empty lists

```
>>> max([], default=0)
0
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
