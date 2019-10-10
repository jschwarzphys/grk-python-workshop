import math
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def length(self):
        return math.sqrt(self.x**2 + self.y**2)
    def scale(self, factor):
        self.x *= factor
        self.y *= factor   

def exp_seq(limit):
    v = 1
    while v < limit:
        yield v
        v *= 2
