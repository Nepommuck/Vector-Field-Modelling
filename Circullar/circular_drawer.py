from pygame import draw, Vector2
from versors import versors


class Circular_drawer:
    def __init__(self, window, center, radiuses, scale, circles):
        self.window = window
        self.center = center
        self.radiuses = radiuses
        self.scale = scale
        self.circles = circles

    def draw_lines(self, length, color=(0, 0, 0, 255)):
        for versor in versors:

            draw.aaline(self.window, color, self.center, self.center + versor * length)

    def draw_points(self, color=(0, 0, 0, 255), point_rad=5):
        for versor in versors:
            for radius in self.radiuses:
                draw.circle(self.window, color, self.center + versor * radius * self.scale, point_rad)

    def draw_circles(self, color=(0, 0, 0, 255), width=1):
        for point, rad in self.circles:
            draw.circle(self.window, color, self.center + point * self.scale, rad * self.scale, width)