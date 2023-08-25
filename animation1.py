from vector import Vector
from engine import run
from ball import Ball
from wall import Wall
from random import uniform

width = 100
height = 50
unit_length = 10

objects = [
    Wall(
        Vector(-width/4, -height/3),
        Vector(-width/4, height/3)
    ),
    Wall(
        Vector(width/4, -height/3),
        Vector(width/4, height/3)
    ),
    Wall(
        Vector(-width/4, height/3),
        Vector(width/4, height/3)
    ),
    Wall(
        Vector(-width/4, -height/3),
        Vector(width/4, -height/3),
    ),

    Ball(
        2.5,
        Vector(-6, 6),
        Vector(3,-3) + Vector(uniform(-0.1, 0.1), uniform(-0.1, 0.1)),
        1
    ),
    Ball(
        2.5,
        Vector(0, 6),
        Vector(0,-3) + Vector(uniform(-0.1, 0.1), uniform(-0.1, 0.1)) ,
        1
    ),
    Ball(
        2.5,
        Vector(6, 6),
        Vector(-3,-3) + Vector(uniform(-0.1, 0.1), uniform(-0.1, 0.1)),
        1
    ),
    Ball(
        2.5,
        Vector(-6, 0),
        Vector(3,0) + Vector(uniform(-0.1, 0.1), uniform(-0.1, 0.1)),
        1
    ),
    Ball(
        2.5,
        Vector(0, 0),
        Vector(0,0) + Vector(uniform(-0.1, 0.1), uniform(-0.1, 0.1)),
        1
    ),
    Ball(
        2.5,
        Vector(6, 0),
        Vector(-3,0) + Vector(uniform(-0.1, 0.1), uniform(-0.1, 0.1)),
        1
    ),
    Ball(
        2.5,
        Vector(-6,-6),
        Vector(3,3) + Vector(uniform(-0.1, 0.1), uniform(-0.1, 0.1)),
        1
    ),
    Ball(
        2.5,
        Vector(0,-6),
        Vector(0,3) + Vector(uniform(-0.1, 0.1), uniform(-0.1, 0.1)),
        1
    ),
    Ball(
        2.5,
        Vector(6,-6),
        Vector(-3,3) + Vector(uniform(-0.1, 0.1), uniform(-0.1, 0.1)),
        1
    ),
]

run(
    objects, 
    "Animation1", 
    (height * unit_length, width * unit_length, 3),
    10.0,
    120,
    unit_length,
)