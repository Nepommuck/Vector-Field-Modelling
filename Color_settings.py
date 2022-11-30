import pygame


class Color_settings:
    def __init__(self, background, vector_color, vector_color2=None, vector_lengths=(0, 1)):
        self.background = background
        self.vector1 = vector_color
        self.vector2 = vector_color2
        self.d_vector = None if vector_color2 is None else \
            [self.vector2[i] - self.vector1[i] for i in range(len(self.vector1))]

        self.max_length = vector_lengths[1]
        self.min_length = vector_lengths[0]

    def get_vector_color(self, length):
        if self.vector2 is None:
            return self.vector1
        
        if length >= self.max_length:
            return self.vector2
        if length <= self.min_length:
            return self.vector1

        pl = (length - self.min_length) / (self.max_length - self.min_length)
        return tuple([self.vector1[i] + pl * self.d_vector[i] for i in range(len(self.vector1))])
