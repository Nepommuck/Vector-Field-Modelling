class Data_handler:
    def __init__(self, file_name, separators=None):
        file = open(file_name, "r")
        readings = file.read().split(separators)

        self.radiuses = []
        self.field_data = [[] for _ in range(3)]
        i = 0
        for reading in readings:
            if i % 4 == 0:
                self.radiuses.append(float(reading))
            else:
                # self.field_data[-1].append(float(reading))
                self.field_data[(i-1) % 3].append(float(reading))
            i += 1

        self.max = min([row[0] for row in self.field_data])
        self.min = max([row[-1] for row in self.field_data])

    def get_circle_points(self, values):
        return [self.calculate_circle_points(v) for v in values]

    def calculate_circle_points(self, value):
        if not self.min <= value <= self.max:
            return None
        axis_points = []
        for row in self.field_data:
            i = 0
            while row[i] > value:
                i += 1

            if row[i] == value:
                axis_points.append(i)
            else:
                axis_points.append(
                    (i - 1) + (row[i-1] - value) / (row[i-1] - row[i])
                )

        res = []
        for axis_point in axis_points:
            i = int(axis_point)
            rem = axis_point - i
            
            if axis_point == i:
                res.append(self.radiuses[i])
            
            res.append(self.radiuses[i] - rem * (self.radiuses[i] - self.radiuses[i+1]))

        return tuple(res)

