import pygame
from pygame import Vector2
from Color_settings import Color_settings
import circular_field_data
import circular_drawer
from circular_solver import Circular_solver


def cfor(a, b, i):
    res = []
    while a <= b:
        res.append(a)
        a += i
    return res


FPS = 24
SCALE = 5
circle_values = [i for i in range(2, 6 + 1)]
# circle_values = cfor(1.1, 6.5, 1)

if __name__ == '__main__':

    WIN = pygame.display.set_mode((900, 900))
    pygame.display.set_caption("Real Physics here!")

    DH = circular_field_data.Data_handler("circular_readings.txt")

    circles = [Circular_solver().solve_circle_equasion(points) for points in DH.get_circle_points(circle_values)]
    drawer = circular_drawer.Circular_drawer(WIN, Vector2(400, 450), DH.radiuses, 5, circles)

    CS = Color_settings(pygame.Color("white"), pygame.Color("blue"))
    WIN.fill(CS.background)

    print(drawer.radiuses)
    drawer.draw_lines(800)
    drawer.draw_points()
    drawer.draw_circles()

    print(DH.field_data)
    print(
        DH.calculate_circle_points(4.5)
    )

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                print('Program closed')
                pygame.quit()
