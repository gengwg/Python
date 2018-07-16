# 7.8: sort the points according to their distance from some other point

points = [(1,2), (3,4), (5,6), (7,8)]

import math
def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2-x1, y2-y1)

from functools import partial

pt = (4,3)
# the key arg of sort() method only works with func that takea  single argument
points.sort(key=partial(distance, pt))
# can be replaced with a lambda expression
# points.sort(key=lambda p: distance(p, pt))
print(points)   # [(3, 4), (1, 2), (5, 6), (7, 8)]

