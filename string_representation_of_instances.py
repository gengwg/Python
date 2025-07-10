class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # The __repr__ method is used for official string representation
    def __repr__(self):
        return f"Pair({self.x!r}, {self.y!r})"
    
    # The __str__ method is used for informal string representation
    # If __str__ is not defined, Python will use __repr__ as a fallback
    def __str__(self):
        return f"({self.x!s}, {self.y!s})"
    
def main():
    p = Pair(3, 4)

    print(f"p is {p!r}") # Calls __repr__
    print(f"p is {repr(p)}")  # Explicitly calls __repr__
    print(f"p is {p.__repr__()}")  # Explicitly calls __repr__

    print(f"p is {p}")  # Calls __str__
    print(f"p is {str(p)}")  # Explicitly calls __str__     
    print(f"p is {p.__str__()}")  # Explicitly calls __str__
    
if __name__ == "__main__":
    main()