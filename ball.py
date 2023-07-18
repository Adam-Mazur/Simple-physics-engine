from vector import Vector
from math import sqrt
from curve import *
import numpy as np
import cv2 as cv

class Ball:
    default_color = (22, 19, 232)
    animation_color = (232, 65, 19)

    def __init__(self, radius: float, position: Vector, velocity: Vector, mass: float):
        self.radius = radius
        self.position = position
        self.velocity = velocity
        self.mass = mass
        self.animation = Curve(bouncingTap, 30)

    def __call__(self, canvas: np.ndarray, unit_length: float):
        t = self.animation()

        color = (
            sqrt((1 - t) * self.default_color[0]**2 + t * self.animation_color[0]**2),
            sqrt((1 - t) * self.default_color[1]**2 + t * self.animation_color[1]**2),
            sqrt((1 - t) * self.default_color[2]**2 + t * self.animation_color[2]**2),
        )

        cv.circle(
            canvas, 
            (round(self.position.x * unit_length + canvas.shape[1]/2), round(- self.position.y * unit_length + canvas.shape[0]/2)), 
            round(self.radius * unit_length), 
            color, 
            thickness = cv.FILLED
        )

    def update(self, delta_t):
        self.position += self.velocity * delta_t

    def collide(self, delta_t):
        self.animation.start()

        self.update(delta_t)

    def backward(self, delta_t):
        self.position -= self.velocity * delta_t

    @property
    def left(self):
        return self.position.x - self.radius
    
    @property
    def right(self):
        return self.position.x + self.radius