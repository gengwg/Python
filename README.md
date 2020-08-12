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
python3 -m venv myvenv
# or equivalent
pyvenv myvenv

source myvenv/bin/activate

# upgrade pip3
(myvenv) user@host:~$ pip3 --version
pip 9.0.1 from /home/pi/myvenv/lib/python3.5/site-packages (python 3.5)
(myvenv) user@host:~$ python3 -m pip install --upgrade pip
(myvenv) user@host:~$ pip3 --version
pip 20.2.2 from /home/pi/myvenv/lib/python3.5/site-packages/pip (python 3.5)
(myvenv) user@host:~$ pip3 install requests
```

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

