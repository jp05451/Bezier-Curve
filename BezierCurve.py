import pygame
import numpy as np
import math


class BezierCurve:
    def __init__(self, points):
        self.order = len(points) - 1  # Order of the Bezier curve
        self.points = points  # Control points
        self.curve_points = []  # Points on the Bezier curve
        self.selected_point = None  # Currently selected control point

        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))  # Initialize the display
        pygame.display.set_caption("Bezier Curve")  # Set the window title
        self.clock = pygame.time.Clock()  # Clock to control the frame rate

    def draw_points(self):
        # Draw the control points as red circles
        for point in self.points:
            pygame.draw.circle(self.screen, (255, 0, 0), point, 5)

    def draw_curve(self):
        # Draw the Bezier curve as a series of white lines
        self.curve_points = self.calculate_bezier_curve()
        for i in range(len(self.curve_points) - 1):
            pygame.draw.line(
                self.screen,
                (255, 255, 255),
                self.curve_points[i],
                self.curve_points[i + 1],
                2,
            )

    def calculate_bezier_curve(self):
        # Calculate points on the Bezier curve using recursive method
        t_values = np.linspace(0, 1, 100)
        curve_points = [
            self.calculate_bezier_point_recursive(self.points, t) for t in t_values
        ]
        return curve_points

    def calculate_bezier_point_recursive(self, points, t):
        # Recursive function to calculate a point on the Bezier curve
        # Base case: if there's only one point, return it
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
        """
        Calculate the binomial coefficient "n choose k", which is the number of ways
        to choose k elements from a set of n elements without regard to the order.

        Args:
            n (int): The number of elements in the set.
            k (int): The number of elements to choose.

        Returns:
            int: The binomial coefficient.
        """
        return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

    def run(self):
        # Main loop to run the Pygame application
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if a control point is selected
                    self.selected_point = self.get_selected_point(event.pos)
                elif event.type == pygame.MOUSEBUTTONUP:
                    # Deselect the control point
                    self.selected_point = None
                elif (
                    event.type == pygame.MOUSEMOTION and self.selected_point is not None
                ):
                    # Move the selected control point
                    self.points[self.selected_point] = event.pos

            # Clear the screen
            self.screen.fill((0, 0, 0))
            # Draw the control points
            self.draw_points()
            # Draw the Bezier curve
            self.draw_curve()
            # Update the display
            pygame.display.flip()
            # Cap the frame rate
            self.clock.tick(60)

        pygame.quit()

    def get_selected_point(self, pos):
        # Check if the mouse click is close to any of the control points
        for i, point in enumerate(self.points):
            if math.hypot(point[0] - pos[0], point[1] - pos[1]) < 10:
                return i
        return None


if __name__ == "__main__":
    points = [(100, 100), (200, 400), (400, 400), (500, 100)]  # Initial control points
    bezier_curve = BezierCurve(points)
    bezier_curve.run()
