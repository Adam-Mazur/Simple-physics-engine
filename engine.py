from itertools import combinations
from vector import Vector
from ball import Ball
import numpy as np
import cv2 as cv

def run(objects: list, title: str, dim: tuple, delta_t: float, unit_length: float, background_color: tuple = (40, 40, 40)):
    while True:
        canvas = np.empty(dim, dtype='uint8')
        canvas[:] = background_color

        for obj in objects:
            obj(canvas, unit_length)

        cv.imshow(title, canvas)

        # If the key c is pressed, close the window
        if cv.waitKey(20) & 0xFF == ord('c'):
            break

        width = dim[1] / unit_length
        height = dim[0] / unit_length

        # Collisions with the borders 
        for obj in objects:
            if obj.position.x <= - width/2 + obj.radius: 
                obj.velocity.x = abs(obj.velocity.x) 
            if obj.position.x >= width/2 - obj.radius:
                obj.velocity.x = - abs(obj.velocity.x)
            if obj.position.y <= - height/2 + obj.radius:
                obj.velocity.y = abs(obj.velocity.y) 
            if obj.position.y >= height/2 - obj.radius:
                obj.velocity.y = - abs(obj.velocity.y)

        # Collisions with other objects
        potential_collisions = [set()]

        objects.sort(key = lambda x: x.position.x - x.radius)
        for i in range(len(objects) - 1):
            a = objects[i].position.x + objects[i].radius
            b = objects[i + 1].position.x - objects[i + 1].radius

            if b <= a:
                potential_collisions[-1].add(i)
                potential_collisions[-1].add(i + 1)
            else:
                potential_collisions.append(set())

        if len(potential_collisions[-1]) == 0:
            potential_collisions.pop()
            
        for set_of_obj in potential_collisions:
            list_of_obj = list(set_of_obj)
            for a, b in combinations(list_of_obj, 2):
                def is_collided(position1, position2):
                    distance = (position1 - position2).length()
                    sum_radius = objects[a].radius + objects[b].radius
                
                    if distance <= sum_radius: return True
                    else: return False

                if is_collided(objects[a].position, objects[b].position):
                    m1 = objects[a].mass
                    m2 = objects[b].mass
                    u1 = objects[a].velocity
                    u2 = objects[b].velocity

                    if u1.length() > u2.length():
                        position = objects[a].position
                        prev_position = objects[a].previous_position
                        its_a = True
                    else:
                        position = objects[b].position
                        prev_position = objects[b].previous_position
                        its_a = False

                    displacment = position - prev_position
                    counter = 0b0000

                    lookup = [
                        0b1000,
                        0b0100,
                        0b0010,
                        0b0001
                    ]

                    for i in lookup:
                        counter = counter | i

                        if is_collided(
                            prev_position + displacment * counter/15,
                            objects[b].position if its_a else position 
                        ):  counter = counter & (~i)

                    if its_a:
                        objects[a].position = prev_position + displacment * counter/15
                    else:
                        objects[b].position = prev_position + displacment * counter/15

                    objects[a].velocity = (m1 - m2)/(m1 + m2)*u1 + 2*m2/(m1 + m2)*u2
                    objects[b].velocity = 2*m1/(m1 + m2)*u1 + (m2 - m1)/(m1 + m2)*u2

                    objects[a].collide(delta_t * (1 - counter/15))
                    objects[b].collide(delta_t * (1 - counter/15))

        for obj in objects:
            obj.update(delta_t)

    cv.destroyAllWindows()
