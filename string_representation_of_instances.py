class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Pair({self.x!r}, {self.y!r})"
    
    def __str__(self):
        return f"({self.x!s}, {self.y!s})"
    
def main():
    p = Pair(3, 4)

    print(f"p is {p!r}") # Calls __repr__
    print(f"p is {repr(p)}")  # Explicitly calls __repr__

    print(f"p is {p}")  # Calls __str__
    print(f"p is {str(p)}")  # Explicitly calls __str__ 

if __name__ == "__main__":
    main()