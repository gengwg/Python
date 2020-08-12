# Python
Python Cookbooks and Examples


### Creating virtual environments

```
python3 -m venv myvenv
# or equivalent
pyvenv myvenv
source myvenv/bin/activate
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

