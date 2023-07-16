from math import cos

def elasticTap(x):
    return -3.3*(x + 0.533)*(x - 0.706)*(x - 0.412)*(x - 1.002)

def bouncingTap(x):
    return (0.7*x**2 - 1.7 * x + 1) * (cos(7 * x)**2 + 2)/3

class Curve:
    def __init__(self, func, n_steps: float):
        self.func = func
        self.n_steps = n_steps
        self.step = 0
        self.on = False

    def start(self):
        self.on = True
        self.step = 0

    def __call__(self):
        if not self.on:
            return 0
        
        temp = max(min(self.func(self.step/(self.n_steps - 1)), 1), 0)

        self.step += 1
        if self.step == self.n_steps:
            self.step = 0
            self.on = False

        return temp