```
>>> import mymodule
>>> a = mymodule.A()
>>> a.spam()
A.spam()
>>> b = mymodule.B()
>>> b.bar()
B.bar()

>>> from mymodule import A, B
>>> A
<class 'mymodule.a.A'>
>>> B
<class 'mymodule.b.B'>
```
