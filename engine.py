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
                def is_collided(obj1, obj2):
                    distance = (obj1.position - obj2.position).length()
                    sum_radius = obj1.radius + obj2.radius
                
                    if distance <= sum_radius: return True
                    else: return False

                def normal_vector(position: Vector, obj):
                    return (position - obj.position)/(position - obj.position).length()

                if is_collided(objects[a], objects[b]):
                    prev_v = objects[a].velocity

                    objects[a].collide(
                        objects[b].mass,
                        objects[b].velocity,
                        lambda p: is_collided(
                            Ball(
                                objects[a].radius,
                                p,
                                objects[a].velocity,
                                objects[a].mass
                            ),
                            objects[b]
                        ),
                        lambda p: normal_vector(p, objects[b])
                    )
                    objects[b].collide(
                        objects[a].mass,
                        prev_v,
                        lambda p: is_collided(
                            Ball(
                                objects[b].radius,
                                p,
                                objects[b].velocity,
                                objects[b].mass
                            ),
                            objects[a]
                        ),
                        lambda p: normal_vector(p, objects[a])
                    )
                    
        for obj in objects:
            obj.update(delta_t)

    cv.destroyAllWindows()
