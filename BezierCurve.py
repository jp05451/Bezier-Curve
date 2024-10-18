from turtle import Screen, Turtle
import numpy as np
import math

class BezierCurve:
    def __init__(self, points):
        self.order = len(points) - 1
        self.screen = Screen()
        self.screen.setup(width=800, height=600)
        self.screen.tracer(0)  # 關閉動畫
        self.points = [Turtle(shape="circle") for _ in range(4)]
        self.positions = points
        self.curve_turtle = Turtle(visible=False)
        self.curve_turtle.hideturtle()
        
        # 設置點的初始位置
        for point, pos in zip(self.points, self.positions):
            point.penup()
            point.goto(pos)
            point.shapesize(0.5, 0.5)
            point.ondrag(self.create_drag_handler(point))
        
        self.draw_curve()
        self.screen.update()  # 手動更新畫布

    def create_drag_handler(self, point):
        def on_drag(x, y):
            point.goto(x, y)
            self.update_positions()
            self.draw_curve()
            self.screen.update()  # 手動更新畫布
        return on_drag

    def update_positions(self):
        self.positions = [point.pos() for point in self.points]

    def draw_curve(self):
        self.curve_turtle.clear()
        t_values = np.linspace(0, 1, 100)
        curve_points = [self.calculate_bezier_point(t) for t in t_values]
        
        self.curve_turtle.penup()
        self.curve_turtle.goto(curve_points[0])
        self.curve_turtle.pendown()
        
        for point in curve_points:
            self.curve_turtle.goto(point)

    def calculate_bezier_point(self, t):
        n = self.order
        x = sum(self.binomial_coeff(n, i) * (1 - t)**(n - i) * t**i * self.positions[i][0] for i in range(n + 1))
        y = sum(self.binomial_coeff(n, i) * (1 - t)**(n - i) * t**i * self.positions[i][1] for i in range(n + 1))
        return x, y

    @staticmethod
    def binomial_coeff(n, k):
        return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

# 測試 BezierCurve 類
if __name__ == "__main__":
    points = [(-100, 100), (100, 100), (-100, -100), (100, -100)]
    bezier_curve = BezierCurve(points)
    bezier_curve.screen.mainloop()