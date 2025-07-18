import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
    def distance_to(self, other):
        if not isinstance(other, Point):
            raise TypeError("Distance can only be calculated between Point instances")
        return math.hypot(self.x - other.x, self.y - other.y)
    
if __name__ == "__main__":
    p1 = Point(1, 2)
    p2 = Point(4, 6)
    print(f"Distance between {p1} and {p2} is {p1.distance_to(p2)}")
    
    d = getattr(p1, 'distance_to')
    print(f"Distance using getattr: {d(p2)}")

    import operator
    print(f"Distance using operator.methodcaller: {operator.methodcaller('distance_to', p2)(p1)}")

    # Sorting points by distance to the origin using operator.methodcaller
    points = [Point(5, 12), Point(1, 2), Point(3, 4), Point(-4, 3), Point(8, 15), Point(0, 0)]
    # points.sort(key=lambda p: p.distance_to(Point(0, 0)))             # Using lambda
    # points.sort(key=getattr(Point(0,0), 'distance_to'))                 # Using getattr to get the method
    points.sort(key=operator.methodcaller('distance_to', Point(0, 0)))  # Using operator.methodcaller
    print("Points sorted by distance to origin:", points)