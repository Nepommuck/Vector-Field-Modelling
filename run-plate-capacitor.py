import pygame
import os

from pygame import Vector2

import plate_capacitor.console_visualization as console_visualization
import plate_capacitor.vector_drawer as vector_drawer

from common.Color_settings import Color_settings
from plate_capacitor.config import GRAPHICAL_SETTINGS as GS
from plate_capacitor.field_data import Data_handler, Data_reader


FPS = 24


def main():
    WIN = pygame.display.set_mode((GS.WIDTH, GS.HEIGHT))
    pygame.display.set_caption("Real Physics here!")

    data = Data_reader(
        os.path.join("plate_capacitor", "readings.txt")
    ).read_data()
    DH = Data_handler(data)
    dU = DH.calc_dU()

    CS = Color_settings(pygame.Color("white"), pygame.Color("green"), pygame.Color("red"),
                        (DH.get_min_length(), DH.get_max_length()))

    WIN.fill(CS.background)

    for y in range(len(dU)):
        for x in range(len(dU[0])):
            if dU[y][x] is not None:
                if GS.HORIZONTAL:
                    position = Vector2(GS.MARGIN_LEFT + x * GS.PADDING, GS.MARGIN_TOP + y * GS.PADDING)
                    vector = Vector2(dU[y][x])
                else:
                    position = Vector2(GS.MARGIN_LEFT + y * GS.PADDING, GS.MARGIN_TOP + x * GS.PADDING)
                    vector = Vector2(-dU[y][x][1], -dU[y][x][0])

                vector_drawer.draw_vector(
                    WIN, CS.get_vector_color(vector.length()),
                    position,
                    vector * GS.VECTOR_SCALE, GS.VECTOR_TIP_SIZE)

    console_visualization.print_field(data)
    console_visualization.print_dU(dU)

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
