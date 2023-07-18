from vector import Vector
from engine import run
from ball import Ball
from wall import Wall
import random

objects = []

width = 100
height = 50

unit_length = 10


for i in range(2):
    objects.append(
        Wall(
            Vector(
                random.uniform(-width/2, width/2),
                random.uniform(-height/2, height/2)
            ),
            Vector(
                random.uniform(-width/2, width/2),
                random.uniform(-height/2, height/2)
            )
        )
    )

for i in range(10):
    radius = 2
    objects.append(
        Ball(
            radius = radius,
            position = Vector(
                random.uniform(-width/2 + radius, width/2 - radius),
                random.uniform(-height/2 + radius, height/2 - radius)
            ),
            velocity = Vector(
                random.uniform(-4, 4),
                random.uniform(4, 4)
            ),
            mass = 5
        )
    )

run(
    objects, 
    "Animation", 
    (height * unit_length, width * unit_length, 3),
    10.0,
    60,
    unit_length,
)