import numpy as np
import math
import sys
import signal
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


class BezierCurve:
    def __init__(self, points):
        self.order = len(points) - 1
        self.positions = points
        self.selected_point = None
        self.window = None

    def draw_curve(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glColor3f(1.0, 1.0, 1.0)
        glBegin(GL_LINE_STRIP)

        t_values = np.linspace(0, 1, 100)
        for t in t_values:
            x, y = self.calculate_bezier_point(t)
            glVertex2f(x, y)

        glEnd()

        # 繪製控制點
        glColor3f(1.0, 0.0, 0.0)
        glPointSize(10)
        glBegin(GL_POINTS)
        for x, y in self.positions:
            glVertex2f(x, y)
        glEnd()

        glutSwapBuffers()

    # def calculate_bezier_point(self, t):
    #     n = self.order
    #     x = sum(
    #         self.binomial_coeff(n, i) * (1 - t) ** (n - i) * t**i * self.positions[i][0]
    #         for i in range(n + 1)
    #     )
    #     y = sum(
    #         self.binomial_coeff(n, i) * (1 - t) ** (n - i) * t**i * self.positions[i][1]
    #         for i in range(n + 1)
    #     )
    #     return x, y
    
    def calculate_bezier_point(self, t):
        def recursive_bezier(points, t):
            if len(points) == 1:
                return points[0]
            new_points = [
                (
                    (1 - t) * points[i][0] + t * points[i + 1][0],
                    (1 - t) * points[i][1] + t * points[i + 1][1],
                )
                for i in range(len(points) - 1)
            ]
            return recursive_bezier(new_points, t)

        return recursive_bezier(self.positions, t)

    @staticmethod
    def binomial_coeff(n, k):
        return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

    def run(self):
        signal.signal(signal.SIGINT, self.signal_handler)
        glutInit()
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
        glutInitWindowSize(800, 600)
        glutInitWindowPosition(0, 0)
        self.window = glutCreateWindow(b"Bezier Curve with OpenGL")
        glutDisplayFunc(self.draw_curve)
        glutIdleFunc(self.draw_curve)
        glutMouseFunc(self.mouse_button)
        glutMotionFunc(self.mouse_motion)
        self.init_gl(800, 600)
        glutMainLoop()

    def init_gl(self, width, height):
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(-400, 400, -300, 300)
        glMatrixMode(GL_MODELVIEW)

    def mouse_button(self, button, state, x, y):
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            # 將窗口座標轉換為 OpenGL 座標
            ogl_x = (x / 800) * 800 - 400
            ogl_y = (1 - y / 600) * 600 - 300
            for i, (px, py) in enumerate(self.positions):
                if abs(ogl_x - px) < 10 and abs(ogl_y - py) < 10:
                    self.selected_point = i
                    break
        elif button == GLUT_LEFT_BUTTON and state == GLUT_UP:
            self.selected_point = None

    def mouse_motion(self, x, y):
        if self.selected_point is not None:
            # 將窗口座標轉換為 OpenGL 座標
            ogl_x = (x / 800) * 800 - 400
            ogl_y = (1 - y / 600) * 600 - 300
            self.positions[self.selected_point] = (ogl_x, ogl_y)
            glutPostRedisplay()

    def signal_handler(self, sig, frame):
        print("Ctrl+C pressed, exiting...")
        glutDestroyWindow(self.window)
        sys.exit(0)


# 測試 BezierCurve 類
if __name__ == "__main__":
    points = [(-100, 100), (100, 100), (-100, -100), (100, -100)]
    bezier_curve = BezierCurve(points)
    bezier_curve.run()
