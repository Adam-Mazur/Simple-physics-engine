# Testing if the collision detection between balls and the edges of the walls works correctly
from vector import Vector
from engine import run
from ball import Ball
from wall import Wall
from math import sin, cos, pi

objects = []

width = 100
height = 50

unit_length = 10


objects.append(
    Wall(
        Vector(0, 0),
        Vector(width * 0.4, 0)
    )
)
    
angle = pi * 0.32

objects.append(
    Ball(
        radius = 2,
        position = Vector(- 20 * cos(angle) - 1.2, 20 * sin(angle)),
        velocity = Vector(5 * cos(angle), - 5 * sin(angle)),
        mass = 5
    )
)

run(
    objects, 
    "Animation", 
    (height * unit_length, width * unit_length, 3),
    10,
    60,
    unit_length,
)