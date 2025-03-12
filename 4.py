import numpy as np

points = input().split()


def distance(x1, y1, x2, y2):
    print(np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))

distance(float(points[0]), float(points[1]), float(points[2]), float(points[3]))