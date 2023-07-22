from itertools import combinations
from math import sqrt
from vector import Vector
from ball import Ball
from wall import Wall
import numpy as np
import cv2 as cv

def collision(obj1, obj2, delta_t):
    def is_collided(obj1, obj2):
        if isinstance(obj1, Ball) and isinstance(obj2, Ball):
            distance = (obj1.position - obj2.position).length()
            sum_radius = obj1.radius + obj2.radius
    
            if distance <= sum_radius: return True
            else: return False
        elif isinstance(obj1, Ball) and isinstance(obj2, Wall):
            ball = obj1
            wall = obj2
        elif isinstance(obj1, Wall) and isinstance(obj2, Ball):
            ball = obj2
            wall = obj1
        elif isinstance(obj1, Wall) and isinstance(obj2, Wall):
            return False
        else:
            raise ValueError("Two objects are neither an instance of the Ball object nor the Wall object.")

        d = wall.p2 - wall.p1
        f = wall.p1 - ball.position

        a = d.dot(d)
        b = 2 * f.dot(d)
        c = f.dot(f) - ball.radius**2

        discriminant = b**2 - 4*a*c

        if discriminant < 0:
            return False

        discriminant = sqrt(discriminant)

        t1 = (-b - discriminant)/(2*a)
        t2 = (-b + discriminant)/(2*a)

        if t1 >= 0 and t1 <= 1 or t2 >= 0 and t2 <= 1:
            return True
        else:
            return False        

    if is_collided(obj1, obj2):
        prev_position1 = obj1.position
        prev_position2 = obj2.position

        obj1.backward(delta_t)
        obj2.backward(delta_t)

        counter = 0
        power = 5
        for j in range(power, -1, -1):
            i = 2**j
            counter = counter | i
            obj1.update(delta_t * i/(2**(power+1)-1))
            obj2.update(delta_t * i/(2**(power+1)-1))
            if is_collided(obj1, obj2):
                counter = counter & (~i)
                obj1.backward(delta_t * i/(2**(power+1)-1))
                obj2.backward(delta_t * i/(2**(power+1)-1))

        if isinstance(obj1, Ball) and isinstance(obj2, Ball):
            x1 = obj1.position
            x2 = obj2.position
            m1 = obj1.mass
            m2 = obj2.mass
            u1 = obj1.velocity
            u2 = obj2.velocity

            # Formulas taken from https://en.wikipedia.org/wiki/Elastic_collision#Two-dimensional_collision_with_two_moving_objects
            obj1.velocity = u1 - 2*m2/(m1 + m2) * (u1 - u2).dot(x1 - x2) / (x1 - x2).length()**2 * (x1 - x2)
            obj2.velocity = u2 - 2*m1/(m1 + m2) * (u2 - u1).dot(x2 - x1) / (x2 - x1).length()**2 * (x2 - x1)
        else:
            if isinstance(obj1, Ball) and isinstance(obj2, Wall):
                prev_position = prev_position1
                ball = obj1
                wall = obj2
            elif isinstance(obj1, Wall) and isinstance(obj2, Ball):
                prev_position = prev_position2
                ball = obj2
                wall = obj1
            else:
                raise ValueError(f"Objects {type(obj1)} and {type(obj2)} don't match the required types.")
            
            wall_vec = (wall.p2 - wall.p1)/(wall.p2 - wall.p1).length()
            n = Vector(-wall_vec.y, wall_vec.x)
            v = ball.velocity

            proj_n = v.dot(n)/n.dot(n)*n

            d1 = (prev_position - wall.p1).length()
            d2 = (prev_position - wall.p2).length()
            d = (wall.p1 - wall.p2).length()

            if d1 < ball.radius and d2 > d:
                ball.velocity = v - 2*v.dot(prev_position - wall.p1)/(prev_position - wall.p1).length()**2 * (prev_position - wall.p1) 
            elif d2 < ball.radius and d1 > d:
                ball.velocity = v - 2*v.dot(prev_position - wall.p2)/(prev_position - wall.p2).length()**2 * (prev_position - wall.p2) 
            else:
                ball.velocity = v - 2 * proj_n

        
        obj1.collide(delta_t * (1 - counter/(2**(power+1)-1)))
        obj2.collide(delta_t * (1 - counter/(2**(power+1)-1)))


def run(objects: list, title: str, dim: tuple, speed: float, fps: int, unit_length: float, background_color: tuple = (40, 40, 40)):
    delta_t = speed * (1/fps)
    while True:
        canvas = np.empty(dim, dtype='uint8')
        canvas[:] = background_color

        for obj in objects:
            obj(canvas, unit_length)

        cv.imshow(title, canvas)

        # If the key c is pressed, close the window
        if cv.waitKey(round(1000/fps)) & 0xFF == ord('c'):
            break

        for obj in objects:
            obj.update(delta_t)

        width = dim[1] / unit_length
        height = dim[0] / unit_length

        # Collisions with the borders 
        for obj in objects:
            if isinstance(obj, Ball):
                if obj.position.x <= - width/2 + obj.radius: 
                    obj.velocity.x = abs(obj.velocity.x)
                if obj.position.x >= width/2 - obj.radius:
                    obj.velocity.x = - abs(obj.velocity.x)
                if obj.position.y <= - height/2 + obj.radius:
                    obj.velocity.y = abs(obj.velocity.y) 
                if obj.position.y >= height/2 - obj.radius:
                    obj.velocity.y = - abs(obj.velocity.y)

        # Collisions with other objects
        potential_collisions = []
        objects.sort(key = lambda x: x.left)
        active_interval_right = objects[0].right

        active_interval = {0}

        for i in range(1, len(objects)):
            a = objects[i].left
            b = objects[i].right

            if a <= active_interval_right:
                active_interval.add(i)
            else:
                if len(active_interval) > 1:
                    potential_collisions.append(active_interval)
                active_interval = {i}
            
            if b > active_interval_right:
                active_interval_right = b

        if len(active_interval) > 1:
            potential_collisions.append(active_interval)
            
            
        for set_of_obj in potential_collisions:
            list_of_obj = list(set_of_obj)
            for a, b in combinations(list_of_obj, 2):
                collision(objects[a], objects[b], delta_t)

    cv.destroyAllWindows()
