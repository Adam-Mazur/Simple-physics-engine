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
        Vector(-width/4, 5),
        Vector(width/4, 5)
    ),
    Wall(
        Vector(-width/4, -5),
        Vector(width/4, -5)
    ),
    Wall(
        Vector(-width/4, 5),
        Vector(-width/4-5, 10)
    ),
    Wall(
        Vector(-width/4, -5),
        Vector(-width/4-5, -10)
    ),
    Wall(
        Vector(width/4, 5),
        Vector(width/4+5, 10)
    ),
    Wall(
        Vector(width/4, -5),
        Vector(width/4+5, -10)
    ),

    Ball(
        1.5,
        Vector(-width/3, height/3),
        Vector(uniform(-5,5), uniform(-5,5)),
        10
    ),
    Ball(
        1.5,
        Vector(-width/2.5, height/3.5),
        Vector(uniform(-5,5), uniform(-5,5)),
        10
    ),
    Ball(
        1.5,
        Vector(-width/3.5, 0),
        Vector(uniform(-5,5), uniform(-5,5)),
        10
    ),
    Ball(
        1.5,
        Vector(-width/2.5, -height/3),
        Vector(uniform(-5,5), uniform(-5,5)),
        10
    ),
    Ball(
        1.5,
        Vector(width/3, height/3),
        Vector(uniform(-5,5), uniform(-5,5)),
        10
    ),
    Ball(
        1.5,
        Vector(width/2.5, height/3.5),
        Vector(uniform(-5,5), uniform(-5,5)),
        10
    ),
    Ball(
        1.5,
        Vector(width/3.5, 0),
        Vector(uniform(-5,5), uniform(-5,5)),
        10
    ),
    Ball(
        1.5,
        Vector(width/2.5, -height/3),
        Vector(uniform(-5,5), uniform(-5,5)),
        10
    ),
    Ball(
        1.5,
        Vector(-width/3+5, height/3-4),
        Vector(uniform(-5,5), uniform(-5,5)),
        10
    ),
    Ball(
        1.5,
        Vector(-width/2.5+2, height/3.5-3),
        Vector(uniform(-5,5), uniform(-5,5)),
        10
    ),
    Ball(
        1.5,
        Vector(-width/3.5+2, -3),
        Vector(uniform(-5,5), uniform(-5,5)),
        10
    ),
    Ball(
        1.5,
        Vector(-width/2.5+2, -height/3+5),
        Vector(uniform(-5,5), uniform(-5,5)),
        10
    ),
    Ball(
        1.5,
        Vector(width/3+2, height/3-4),
        Vector(uniform(-5,5), uniform(-5,5)),
        10
    ),
    Ball(
        1.5,
        Vector(width/2.5+3, height/3.5+3),
        Vector(uniform(-5,5), uniform(-5,5)),
        10
    ),
    Ball(
        1.5,
        Vector(width/3.5+3, -3),
        Vector(uniform(-5,5), uniform(-5,5)),
        10
    ),
    Ball(
        1.5,
        Vector(width/2.5+5, -height/3-4),
        Vector(uniform(-5,5), uniform(-5,5)),
        10
    ),
]

run(
    objects, 
    "Animation2", 
    (height * unit_length, width * unit_length, 3),
    10.0,
    120,
    unit_length,
)