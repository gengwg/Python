# This script demonstrates how to call a parent class's method using super() in Python.

class A:
    def spam(self):
        print("A.spam() called")
    
class B(A):
    # Override the spam method in class B
    # This allows B to extend or modify the behavior of A's spam method.
    # If B does not override spam, it will inherit A's spam method.
    # If B overrides spam, it can still call A's spam method using super().
    def spam(self):
        print("B.spam() called")
        super().spam()

    def eggs(self):
        print("B.eggs() called")
        # You can also call A's eggs method if it exists
        super().spam()  # Uncomment if A has an eggs method to call it

class C:
    def __init__(self):
        self.x = 0

class D(C):
    def __init__(self):
        # Call the parent class's constructor to initialize x
        # This is necessary to ensure that the x attribute is initialized properly.
        # If you don't call super().__init__(), x will not be initialized.
        # super() refers to the parent class of D, which is C.
        # This is a common pattern in Python to ensure that the parent class's constructor is called.
        # This allows D to inherit the properties and methods of C.
        # In this case, D inherits from C, so calling super().__init__() initializes
        # the x attribute defined in C.
        # If D had its own __init__ method without calling super().__init__(),
        # the x attribute would not be initialized, leading to potential errors.
        # This is a good practice to ensure that the parent class's initialization logic is executed.
        super().__init__() 
        self.y = 1

# The following classes demonstrate multiple inheritance and method resolution order (MRO).

class E:
    def spam(self):
        print("E.spam() called")
        super().spam()

class F():
    def spam(self):
        print("F.spam() called")

class G(E, F):
    # G inherits from both E and F.
    # If G calls super().spam(), it will follow the method resolution order (MRO).
    # In this case, it will call E's spam method first, then F's spam method.
    def spam(self):
        print("G.spam() called")
        super().spam()
        print(G.__mro__)  # Print the method resolution order for debugging

# The following classes demonstrate the use of super() in a more complex inheritance scenario.
# This shows how to call parent class methods in a diamond-shaped inheritance structure.
# In this case, J inherits from both H and I, which both inherit from Base.
# The method resolution order (MRO) will determine the order in which the parent class methods
# are called when super() is used.

class Base:
    def __init__(self):
        print("Base initialized")

class H(Base):
    def __init__(self):
        super().__init__()  # Calls Base's __init__ method
        print("H initialized")

class I(Base):
    def __init__(self):
        super().__init__()  # Calls Base's __init__ method
        print("I initialized")

class J(H, I):
    def __init__(self):
        super().__init__()  # Calls H's __init__, which calls Base's __init__
        print("J initialized")

if __name__ == "__main__":
    a = A()
    a.spam()  # Calls A's spam method directly

    b = B()
    b.spam()  # Calls B's spam method, which calls A's spam method via super()
    b.eggs()  # Calls B's eggs method, which calls A's spam method via super()

    d = D()
    print(d.x)  # Accesses C's x attribute
    print(d.y)  # Accesses D's y attribute
    d.x = 10  # Modifies C's x attribute
    print(d.x)  # Prints the modified value of C's x attribute
    d.y = 20  # Modifies D's y attribute
    print(d.y)  # Prints the modified value of D's y attribute

    e = E()
    try: 
        e.spam()  # Calls E's spam method, which attempts to call super().
        # Note: E does not inherit from any class, so super() will not find a parent class with a spam method.
        # This will raise an AttributeError if E's parent class does not have a spam method.
    except AttributeError as ex:
        print(f"Error: {ex}")
    
    g = G()
    g.spam()  # Calls G's spam method, which calls E's spam method
    # If E's spam method calls super().spam(), it will look for the next class in the MRO, which is F.
    # So it will print "E.spam() called" followed by "F.spam() called".

    j = J()
    # This will initialize H, which initializes Base, and then I, which also initializes Base
    # Finally, it initializes J.
    # The output will show the order of initialization and the method resolution order.
    print(J.__mro__)  # Print the method resolution order for J
    # This will show the order in which methods are resolved for class J.
    # The MRO will be: J -> H -> I -> Base
    # This means that when you call a method on J, Python will first look in J,
    # then in H, then in I, and finally in Base.