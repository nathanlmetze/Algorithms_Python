# Convex Hull Graham Scan
# By Nathan M
# ASSUME ARRAY OF POINTS IS PROVIDED
def compare(point1, point2):
    conditional = (point1[1] > point2[1]) - (point1[1] < point2[1])
    return conditional if conditional != 0 else (point1[0] > point2[0]) - (point1[0] < point2[0])

def product(point1, point2, point3):
    return (point2[0] - point1[0]) * (point3[1] - point1[1]) - (point2[1] - point1[1]) * (point3[0] - point1[0])

def convex_hull(points):
    hull = []
    points = sorted(points, cmp=compare)
    left_point = points[0]
    final_point = points[0]
    while (len(hull) == 0 or hull[0] != final_point):
        hull_point = final_point
        hull.append(hull_point)
        final_point = left_point
        for point in points:
            if final_point == hull_point or product(hull[-1], final_point, point) < 0:
                final_point = point
    return hull
