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
        self.order = len(points) - 1
        self.screen = Screen()
        self.screen.setup(width=800, height=600)
        self.points=[]
        # 創建四個點
        for p in points:
            temp=Point(p[0],p[1])
            # 綁定拖曳事件
            temp.point.ondrag(lambda x, y, p=temp.point: self.on_drag(x, y, p))
            # storge object Point
            self.points.append(temp)
            
        # self.positions = [(-100, 100), (100, 100), (-100, -100), (100, -100)]

        # 設置點的初始位置
        # for point in  points:
        #     point.penup()
        #     point.goto(pos)
        #     point.shapesize(0.5, 0.5)
        #     # 綁定拖曳事件
        #     point.ondrag(lambda x, y, p=point: self.on_drag(x, y, p))

    def on_drag(self, x, y, point):
        print(f"drag: {x},{y}")
        point.ondrag(None)  # 防止遞歸調用
        point.goto(x, y)
        point.ondrag(lambda x, y: self.on_drag(x, y, point))


# 測試 BezierCurve 類
if __name__ == "__main__":
    points = [(-100, 100), (100, 100), (-100, -100), (100, -100)]
    bezier_curve = BezierCurve(points)
    bezier_curve.screen.mainloop()
