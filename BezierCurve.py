import pygame
import numpy as np
import math

class BezierCurve:
    def __init__(self, points):
        self.order = len(points) - 1
        self.points = points
        self.curve_points = []
        self.selected_point = None

        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Bezier Curve")
        self.clock = pygame.time.Clock()

    def draw_points(self):
        for point in self.points:
            pygame.draw.circle(self.screen, (255, 0, 0), point, 5)

    def draw_curve(self):
        self.curve_points = self.calculate_bezier_curve()
        for i in range(len(self.curve_points) - 1):
            pygame.draw.line(self.screen, (255, 255, 255), self.curve_points[i], self.curve_points[i + 1], 2)

    def calculate_bezier_curve(self):
        t_values = np.linspace(0, 1, 100)
        curve_points = [self.calculate_bezier_point(t) for t in t_values]
        return curve_points

    def calculate_bezier_point(self, t):
        n = self.order
        x = sum(self.binomial_coeff(n, i) * (1 - t)**(n - i) * t**i * self.points[i][0] for i in range(n + 1))
        y = sum(self.binomial_coeff(n, i) * (1 - t)**(n - i) * t**i * self.points[i][1] for i in range(n + 1))
        return x, y

    @staticmethod
    def binomial_coeff(n, k):
        return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.selected_point = self.get_selected_point(event.pos)
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.selected_point = None
                elif event.type == pygame.MOUSEMOTION and self.selected_point is not None:
                    self.points[self.selected_point] = event.pos

            self.screen.fill((0, 0, 0))
            self.draw_points()
            self.draw_curve()
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

    def get_selected_point(self, pos):
        for i, point in enumerate(self.points):
            if math.hypot(point[0] - pos[0], point[1] - pos[1]) < 10:
                return i
        return None

if __name__ == "__main__":
    points = [(100, 100), (200, 400), (400, 400), (500, 100)]
    bezier_curve = BezierCurve(points)
    bezier_curve.run()