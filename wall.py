from vector import Vector
import numpy as np
import cv2 as cv
from math import inf

class Wall:
    color = (100, 100, 100)
    thickness = 2
    mass = inf

    @property
    def velocity(self):
        return Vector(0, 0)
    
    @velocity.setter
    def velocity(self, _):
        pass

    def __init__(self, p1: Vector, p2: Vector):
        self.p1 = p1
        self.p2 = p2

    def __call__(self, canvas: np.ndarray, unit_length: float):
        cv.line(
            canvas,
            (round(self.p1.x * unit_length + canvas.shape[1]/2), round(- self.p1.y * unit_length + canvas.shape[0]/2)),
            (round(self.p2.x * unit_length + canvas.shape[1]/2), round(- self.p2.y * unit_length + canvas.shape[0]/2)),
            self.color,
            self.thickness
        )

    def update(self, _):
        pass

    def collide(self, _):
        pass

    def backward(self, _):
        pass

    @property
    def left(self):
        return min(self.p1.x, self.p2.x)
    
    @property
    def right(self):
        return max(self.p1.x, self.p2.x)