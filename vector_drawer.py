from pygame import Vector2, draw


def draw_line_by_polar(surface, color, start_point, angle, length, width=1):
    v = Vector2()

    v.from_polar((length, angle))

    if width > 1:
        draw.line(surface, color, start_point, start_point + v, width)
    else:
        draw.aaline(surface, color, start_point, start_point + v)


def draw_vector_points(surface, color, start_point, end_point, tip_length=30, width=1):
    (_, angle) = Vector2(
        Vector2(end_point) - Vector2(start_point)
    ).as_polar()

    if width > 1:
        draw.line(surface, color, start_point, end_point, width)
    else:
        draw.aaline(surface, color, start_point, end_point)

    draw_line_by_polar(surface, color, end_point, angle + 45 - 180, tip_length, width)
    draw_line_by_polar(surface, color, end_point, angle - 45 - 180, tip_length, width)


def draw_vector(surface, color, start_point, vector, tip_length=30, width=1):
    end_point = start_point + vector
    draw_vector_points(surface, color, start_point, end_point, tip_length, width)
