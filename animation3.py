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
        Vector(-40, -20),
        Vector(-40, 0),
    ),
    Wall(
        Vector(40, 20),
        Vector(40, 0),
    ),
    Wall(
        Vector(-30, 15),
        Vector(-5, 15),
    ),
    Wall(
        Vector(5, -15),
        Vector(30, -15),
    ),
    Wall(
        Vector(-10, -20),
        Vector(-10, -5),
    ),
    Wall(
        Vector(10, 20),
        Vector(10, 5),
    ),
    Wall(
        Vector(-5, -20),
        Vector(5, -20),
    ),
    Wall(
        Vector(-5, 20),
        Vector(5, 20),
    ),
    Wall(
        Vector(-20, 5),
        Vector(-20, -5),
    ),
    Wall(
        Vector(20, 5),
        Vector(20, -5),
    ),
    Wall(
        Vector(-3, -5),
        Vector(3, -5),
    ),
    Wall(
        Vector(-3, 5),
        Vector(3, 5),
    ),
    Wall(
        Vector(-5, 3),
        Vector(-5, -3),
    ),
    Wall(
        Vector(5, 3),
        Vector(5, -3),
    ),

    Ball(
        2,
        Vector(-35, -20),
        Vector(uniform(-5,5), uniform(-5,5)),
        4
    ),
    Ball(
        2,
        Vector(-30, -20),
        Vector(uniform(-5,5), uniform(-5,5)),
        4
    ),
    Ball(
        2,
        Vector(-25, -20),
        Vector(uniform(-5,5), uniform(-5,5)),
        4
    ),
    Ball(
        2,
        Vector(-20, -20),
        Vector(uniform(-5,5), uniform(-5,5)),
        4
    ),
    Ball(
        2,
        Vector(35, 20),
        Vector(uniform(-5,5), uniform(-5,5)),
        4
    ),
    Ball(
        2,
        Vector(30, 20),
        Vector(uniform(-5,5), uniform(-5,5)),
        4
    ),
    Ball(
        2,
        Vector(25, 20),
        Vector(uniform(-5,5), uniform(-5,5)),
        4
    ),
    Ball(
        2,
        Vector(20, 20),
        Vector(uniform(-5,5), uniform(-5,5)),
        4
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