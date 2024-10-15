from turtle import Screen, Turtle


class Point:
    def __init__(self, x, y):
        self.point = Turtle(shape="square")
        self.point.penup()
        self.point.goto(x, y)
        self.point.shapesize(0.5, 0.5)
        self.position = (x, y)


class BezierCurve:
    def __init__(self, points):
        self.screen = Screen()
        self.pen = Turtle()
        self.pen.speed(0)
        self.order = len(points) - 1
        self.screen.setup(width=800, height=600)
        self.points = []
        # create points
        for p in points:
            temp = Point(p[0], p[1])
            # bind drag event
            # temp.point.ondrag(lambda x, y, p=temp.point: self.on_drag(x, y, p))
            temp.point.ondrag(lambda x, y, p=temp: self.on_drag(x, y, p))
            # storge object Point
            self.points.append(temp)

    def on_drag(self, x, y, p):
        # p.goto(x, y)
        # p.ondrag(lambda x, y: self.on_drag(x, y, p))
        # p.ondrag(None)  # 防止遞歸調用

        p.point.ondrag(None)  # 防止遞歸調用
        p.point.goto(x, y)
        p.position = p.point.position()
        p.position = (x, y)
        # p.draw(self.points[0].position,self.points[-1].position)
        p.point.ondrag(lambda x, y: self.on_drag(x, y, p))

    def mid_point(self, p1, p2):
        return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

    # def calculate(self,points,level):
    #     self.max_level=3
    #     if level > self.max_level:
    #         self.draw((points[0],points[-1]))
    #     else:
    #         L1 = points[0]
    #         L2 = self.mid_point(points[0], points[1])
    #         H = self.mid_point(points[1], points[2])
    #         R3 = self.mid_point(points[2], points[3])
    #         R4 = points[3]
    #         L3 = self.mid_point(L2, H)
    #         R2 = self.mid_point(R3, H)
    #         L4 = self.mid_point(L3, R2)
    #         R1 = L4
    #         self.calculate((L1, L2, L3, L4), level + 1)
    #         self.calculate((R1, R2, R3, R4), level + 1)

    # def draw(self,point):
    #     self.pen.penup()
    #     self.pen.goto(point[0])
    #     self.pen.pendown()
    #     self.pen.goto(point[1])
    #     self.pen.penup()

    def calculate(self, points, t):
        # x,y=(1-t)**3*points[0] + 3*t*(1-t)**2*points[1] + 3*t**2*(1-t)*points[2] + t**3*points[3]
        # self.pen.penup()
        # self.pen.goto(x,y)
        # self.pen.pendown()
        self.pen.penup()
        self.pen.goto(points[0])
        self.pen.pendown()
        for i in range(11):
            t = i / 10
            x = (
                (1 - t) ** 3 * points[0][0]
                + 3 * t * (1 - t) ** 2 * points[1][0]
                + 3 * t**2 * (1 - t) * points[2][0]
                + t**3 * points[3][0]
            )
            y = (
                (1 - t) ** 3 * points[0][1]
                + 3 * t * (1 - t) ** 2 * points[1][1]
                + 3 * t**2 * (1 - t) * points[2][1]
                + t**3 * points[3][1]
            )
            self.pen.goto(x, y)
        self.pen.penup()

# 測試 BezierCurve class
if __name__ == "__main__":
    points = [(-100, 100), (10, 100), (-10, -100), (100, -100)]
    bezier_curve = BezierCurve((points))
    # bezier_curve.draw((points[0],points[-1]))
    bezier_curve.calculate((points[0], points[1], points[2], points[3]), 1)
    bezier_curve.screen.mainloop()
    # bezier_curve.screen.exitonclick()
