from pygame import Vector2
from versors import versors


class Circular_solver:

    def solve_circle_equasion(self, radiuses):
        return self.solve_math(
            self.calc_points(radiuses)
        )

    def calc_points(self, radiuses):
        res = []
        for versor, r in zip(versors, radiuses):
            res.append(versor * r)
        return res

    def solve_math(self, points):
        v = Vector2
        x1, y1 = points[0].x, points[0].y
        x2, y2 = points[1].x, points[1].y
        x3, y3 = points[2].x, points[2].y

        a1 = - (x1 - x2) / (y1 - y2)
        b1 = (x1**2 + y1**2 - x2**2 - y2**2) / (2 * (y1 - y2))

        a2 = - (x1 - x3) / (y1 - y3)
        b2 = (x1**2 + y1**2 - x3**2 - y3**2) / (2 * (y1 - y3))

        x0 = - (b1 - b2) / (a1 - a2)
        y0 = a1 * x0 + b1

        p = Vector2(x0, y0)
        r = (points[0] - p).length()

        return p, r
