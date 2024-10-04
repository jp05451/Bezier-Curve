from turtle import *

class bezierCurve:
    def __init__(self, controlPoints=4):
        self.controlPoints = controlPoints
        self.numberOfControlPoints = len(controlPoints)
        self.numberOfCurves = self.numberOfControlPoints - 1
        self.curvePoints = []
        self.curvePoints.append(self.controlPoints)
        self.turtle = Turtle()
        
    def calculateCurve(self, t):
        while len(self.curvePoints) < self.numberOfControlPoints:
            newPoints = []
            for i in range(len(self.curvePoints[-1]) - 1):
                x = (1 - t) * self.curvePoints[-1][i][0] + t * self.curvePoints[-1][i + 1][0]
                y = (1 - t) * self.curvePoints[-1][i][1] + t * self.curvePoints[-1][i + 1][1]
                newPoints.append((x, y))
            self.curvePoints.append(newPoints)
        return self.curvePoints[-1][0]
    
    def drawCurve(self, t):
        self.turtle.penup()
        for i in range(100):
            x, y = self.calculateCurve(t)
            self.turtle.goto(x, y)
            self.turtle.pendown()
            t += 0.01
            
if __name__ == '__main__':
    controlPoints = [(0, 0), (100, 200), (200, 200), (300, 0)]
    curve = bezierCurve(controlPoints)
    curve.drawCurve(0)