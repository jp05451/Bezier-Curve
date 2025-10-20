import numpy as np
import math


class BezierCurve:
    def __init__(self, points):
        self.order = len(points) - 1
        self.points = points

    def calculate_bezier_curve(self, num=100):
        t_values = np.linspace(0, 1, num)
        curve_points = [
            self.calculate_bezier_point_recursive(self.points, t) for t in t_values
        ]
        return curve_points

    def calculate_bezier_point_recursive(self, points, t):
        if len(points) == 1:
            return points[0]
        new_points = [
            (
                (1 - t) * points[i][0] + t * points[i + 1][0],
                (1 - t) * points[i][1] + t * points[i + 1][1],
            )
            for i in range(len(points) - 1)
        ]
        return self.calculate_bezier_point_recursive(new_points, t)

    @staticmethod
    def binomial_coeff(n, k):
        return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
