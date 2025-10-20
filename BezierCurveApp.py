import pygame
import math
from BezierCurve import BezierCurve

class BezierCurveApp:
    def __init__(self, points):
        self.points = points
        self.selected_point = None
        self.curve = BezierCurve(points)
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Bezier Curve")
        self.clock = pygame.time.Clock()

    def draw_points(self):
        for point in self.points:
            pygame.draw.circle(self.screen, (255, 0, 0), point, 5)

    def draw_curve(self):
        curve_points = self.curve.calculate_bezier_curve()
        for i in range(len(curve_points) - 1):
            pygame.draw.line(
                self.screen,
                (255, 255, 255),
                curve_points[i],
                curve_points[i + 1],
                2,
            )

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
                    self.curve.points = self.points

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
    app = BezierCurveApp(points)
    app.run()
