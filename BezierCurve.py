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
        # create points
        for p in points:
            temp=Point(p[0],p[1])
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
        p.point.ondrag(lambda x, y: self.on_drag(x, y, p))

    def mid_point(self, p1, p2):
        return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
    
    def calculate(self,points,level):
        self.max_level=5
        if level > self.max_level:
            self.draw((self.points[0].position,self.points[-1].position))
        else:
            pass
    
    def draw(self,point:tuple):
        pass    

# 測試 BezierCurve class
if __name__ == "__main__":
    points = [(-100, 100), (100, 100), (-100, -100), (100, -100)]
    bezier_curve = BezierCurve(points)
    bezier_curve.screen.mainloop()
