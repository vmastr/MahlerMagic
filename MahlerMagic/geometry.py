import math
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

def polar_angle(p0, p1=None):
    if p1 is None:
        p1 = Point(0, 0)
    y_span = p0.y - p1.y
    x_span = p0.x - p1.x
    return math.atan2(y_span, x_span)

def distance(p0, p1=None):
    if p1 is None:
        p1 = Point(0, 0)
    y_span = p0.y - p1.y
    x_span = p0.x - p1.x
    return y_span ** 2 + x_span ** 2

def det(p1, p2, p3):
    return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)


def graham_scan(points):
    points = sorted(points, key=lambda p: (p.y, p.x))
    p0 = points[0]
    sorted_points = sorted(points[1:], key=lambda p: (polar_angle(p, p0), -distance(p, p0)))
    hull = [p0, sorted_points[0]]

    for point in sorted_points[1:]:
        while len(hull) > 1 and det(hull[-2], hull[-1], point) <= 0:
            hull.pop()
        hull.append(point)

    return hull

# Example usage
points = [Point(0, 0), Point(1, 1), Point(2, 2), Point(2, 0), Point(0, 2), Point(2, 3), Point(3, 1)]
hull = graham_scan(points)
print("Convex Hull:", hull)

# Plotting the points and the convex hull
plt.figure()
x_coords = [p.x for p in points]
y_coords = [p.y for p in points]
plt.scatter(x_coords, y_coords)

hull.append(hull[0])  # Close the hull
hx = [p.x for p in hull]
hy = [p.y for p in hull]
plt.plot(hx, hy, 'r-')
plt.show()
