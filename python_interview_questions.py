# 1

class A(object):
    def show(self):
        print('base show')

class B(A):
    def show(self):
        print('derived show')

obj = B()
obj.show()

obj.__class__ = A
obj.show()
obj.__class__ = B
obj.show()


# 2
print('-' * 32)

class A(object):
    def __init__(self,a,b):
        self.__a = a
        self.__b = b
    def myprint(self):
        print('a=', self.__a, 'b=', self.__b)

    def __call__(self, num):
        print('call:', num + self.__a)


a1=A(10,20)
a1.myprint()

a1(80)

# 3
print('-' * 32)
class B(object):
    def fn(self):
        print 'B fn'
    def __init__(self):
        print "B INIT"


class A(object):
    def fn(self):
        print 'A fn'

    def __new__(cls,a):
            print "NEW", a
            if a>10:
                return super(A, cls).__new__(cls)
            return B()

    def __init__(self,a):
        print "INIT", a

a1 = A(5)
a1.fn()
a2=A(20)
a2.fn()

# 4
print('-' * 32)

ls = [1,2,3,4]
list1 = [i for i in ls if i>2]
print list1 # [3,4]

list2 = [i*2 for i in ls if i>2]
print list2 # [6, 8]

dic1 = {x: x**2 for x in (2, 4, 6)}
print dic1  # {2: 4, 4: 16, 6, 36}

dic2 = {x: 'item' + str(x**2) for x in (2, 4, 6)}
print dic2  # {2: 'item4', '4': 'item16', 6: 'item36'}

set1 = {x for x in 'hello world' if x not in 'low level'}
print set1  # set(['h', 'r', 'd'])

# 5. local/global variable

print('-' * 32)

num = 9
def f1():
    num = 20

def f2():
    print num


f2()
f1()
f2()
# -------------------
num = 9

def f1():
    global num
    num = 20

def f2():
    print num

f2()
f1()
f2()

# 6. swap val of two variables
print('-' * 32)

a = 8
b = 9
a, b = b, a
print a, b

# 7
print('-' * 32)

class A(object):
    def __init__(self,a,b):
        self.a1 = a
        self.b1 = b
        print 'init'
    def mydefault(self, *args):
        print 'default: ' + str(args[0])
    def __getattr__(self, name):
        print "other fn:", name
        return self.mydefault

a1 = A(10,20)
a1.fn1(33)
a1.fn2('hello')
a1.fn3(10)

# 8. package managment

# only import mod1, mod3

# demopack/
# |-- __init__.py
# |-- mod1.py
# |-- mod2.py
# `-- mod3.py
#
# $ cat demopack/__init__.py
# __all__ = ['mod1', 'mod3' ]

# 9. closure
print('-' * 32)


def mulby(num):
    def gn(val):
        return num * val
    return gn

zw = mulby(7)
print(zw(9))


# 10. performance
print('-' * 32)

# str is immutable. every time a new str is created to store new string.
def strtest1(num):
    str='first'
    for i in range(num):
        str+="X"
    return str

print strtest1(100)
