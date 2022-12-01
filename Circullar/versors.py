from pygame import Vector2


versors = []
for i in range(3):
    v = Vector2()
    v.from_polar((1, 120 * i))
    versors.append(v)
