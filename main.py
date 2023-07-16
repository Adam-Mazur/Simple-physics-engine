from vector import Vector
from engine import run
from ball import Ball
import random

objects = [
    # Ball(
    #     15,
    #     Vector(-30, 0),
    #     Vector(10, 0),
    #     10
    # ),
    # Ball(
    #     10,
    #     Vector(30, 0),
    #     Vector(-10, 0),
    #     10
    # ),
]

width = 100
height = 50

unit_length = 10

delta_t = 0.2

for i in range(25):
    radius = random.uniform(1, 3)
    objects.append(
        Ball(
            radius = radius,
            position = Vector(
                random.uniform(-width/2 + radius, width/2 - radius),
                random.uniform(-height/2 + radius, height/2 - radius)
            ),
            velocity = Vector(
                random.uniform(-4, 4),
                random.uniform(-4, 4)
            ),
            mass = random.uniform(5, 10)
        )
    )

run(
    objects, 
    "Animation", 
    (height * unit_length, width * unit_length, 3),
    delta_t,
    unit_length,
)