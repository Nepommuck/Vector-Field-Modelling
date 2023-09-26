import math

from pygame import Vector2


SMALL_ROW = [False for _ in range(7)] + [True for _ in range(3)]
FULL_ROW = [(i % 2 == 0) for i in range(7)] + [True for _ in range(3)]

BASIC_STRUCTURE = [SMALL_ROW for _ in range(8)] + [FULL_ROW for _ in range(6)] + [SMALL_ROW for _ in range(8)]


class Data_reader:
    def __init__(self, file, structure=None, separators=None):
        if structure is None:
            structure = BASIC_STRUCTURE
        self.structure = structure
        self.file = file
        self.sep = separators

    def read_data(self):
        file = open(self.file, "r")
        readings = file.read().split(sep=self.sep)
        data = [[None for _ in self.structure[0]] for _ in self.structure]

        i = 0
        for y in range(len(self.structure)):
            for x in range(len(self.structure[0])):
                if self.structure[y][x]:
                    data[y][x] = float(readings[i])
                    i += 1
        return data


class Data_handler:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])
        self.dU = None

    def calc_dU(self):
        dU = []
        for y in range(self.rows):
            dU.append([])
            for x in range(self.cols):
                res = None
                if self.data[y][x] is not None:
                    du_dy = None
                    dy = 1
                    while True:
                        if y + dy >= self.rows:
                            break
                        elif self.data[y + dy][x] is not None:
                            du_dy = (self.data[y + dy][x] - self.data[y][x]) / dy
                            break
                        dy += 1

                    if du_dy is not None:
                        du_dx = None
                        dx = 1
                        while True:
                            if x + dx >= self.cols:
                                break
                            elif self.data[y][x + dx] is not None:
                                du_dx = (self.data[y][x + dx] - self.data[y][x]) / dx
                                break
                            dx += 1

                        if du_dx is not None:
                            res = (du_dx, du_dy)

                dU[y].append(res)
        self.dU = dU
        return dU

    def get_min_length(self):
        rez = math.inf
        if self.dU is None:
            return rez

        for row in self.dU:
            for item in row:
                if item is not None:
                    rez = min(rez, Vector2(item).length())
        return rez

    def get_max_length(self):
        rez = 0
        if self.dU is None:
            return rez

        for row in self.dU:
            for item in row:
                if item is not None:
                    rez = max(rez, Vector2(item).length())
        return rez
