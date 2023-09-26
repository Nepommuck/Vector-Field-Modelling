import pygame
import circular_field_data
import circular_drawer
import config as config

from pygame import Vector2
from plate_capacitor.Color_settings import Color_settings
from circular_solver import Circular_solver

FPS = 24


def cfor(a, b, i=1.0):
    res = []
    while a <= b:
        res.append(a)
        a += i
    return res


big_circles_values = cfor(config.MN, config.MX, 2 * config.DV)
small_circles_values = cfor(config.MN + config.DV, config.MX, 2 * config.DV)


def main():
    WIN = pygame.display.set_mode((config.SCREEN_SIZE, config.SCREEN_SIZE))
    pygame.display.set_caption("Real Physics here!")

    DH = circular_field_data.Data_handler("readings.txt")

    circles = [Circular_solver().solve_circle_equasion(points) for points in DH.get_circle_points(big_circles_values)]
    drawer = circular_drawer.Circular_drawer(WIN, Vector2(config.SCREEN_SIZE / 2, config.SCREEN_SIZE / 2), DH.radiuses,
                                             config.SCALE, circles)

    CS = Color_settings(pygame.Color("white"), pygame.Color("blue"))
    WIN.fill(CS.background)

    print("Loaded radiuses:")
    print(drawer.radiuses, end="\n\n")

    drawer.draw_lines(config.SCREEN_SIZE)
    drawer.draw_points(color=pygame.Color("Red"))

    drawer.draw_circles(width=2)

    circles_small = \
        [Circular_solver().solve_circle_equasion(points) for points in DH.get_circle_points(small_circles_values)]
    drawer.circles = circles_small
    drawer.draw_circles(width=1)

    print("Loaded readings:")
    for index, column in enumerate(DH.field_data):
        print(f"Column {index + 1}:  {column}")

    DH.calculate_circle_points(config.SCALE)

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


if __name__ == '__main__':
    main()
