# Testing if the collision between two balls work correctly
from vector import Vector
from engine import run
from ball import Ball
from wall import Wall

objects = []

width = 100
height = 50

unit_length = 10

objects.append(
    Ball(
        radius = 2,
        position = Vector(- width* 0.4, 0),
        velocity = Vector(5, 0),
        mass = 5
    )
)

objects.append(
    Ball(
        radius = 2,
        position = Vector(width * 0.4, 1.5),
        velocity = Vector(-5, 0),
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