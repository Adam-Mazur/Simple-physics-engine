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
        self._position = position
        self.previous_position = position
        self.velocity = velocity
        self.mass = mass
        self.animation = Curve(bouncingTap, 30)

    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, value):
        self.previous_position = self.position
        self._position = value

    def __call__(self, canvas: np.ndarray, unit_length: float):
        t = self.animation()

        color = (
            sqrt((1 - t) * self.default_color[0]**2 + t * self.animation_color[0]**2),
            sqrt((1 - t) * self.default_color[1]**2 + t * self.animation_color[1]**2),
            sqrt((1 - t) * self.default_color[2]**2 + t * self.animation_color[2]**2),
        )

        cv.circle(
            canvas, 
            (round(self.position.x * unit_length + canvas.shape[1]//2), round(- self.position.y * unit_length + canvas.shape[0]//2)), 
            round(self.radius * unit_length), 
            color, 
            thickness = cv.FILLED
        )

    def update(self, delta_t):
        self.previous_position = self.position
        self.position += self.velocity * delta_t

    def collide(self, m2: float, u2: Vector, overlap_func, normal_vector):
        self.animation.start()
        m1 = self.mass
        u1 = self.velocity

        self.velocity = (m1 - m2)/(m1 + m2)*u1 + 2*m2/(m1 + m2)*u2

        displacment = self.position - self.previous_position
        counter = 0b0000

        lookup = [
            0b1000,
            0b0100,
            0b0010,
            0b0001
        ]

        for i in lookup:
            counter = counter | i

            if overlap_func(self.previous_position + displacment * counter/15):
                counter = counter & (~i)

        collision_point = self.previous_position + displacment * counter/15

        temp_vect = self.position - collision_point

        normal = normal_vector(collision_point)

        self.position = collision_point + temp_vect - 2 * temp_vect.dot(normal)/normal.dot(normal) * normal

