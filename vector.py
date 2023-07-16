class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __iadd__(self, other):
        return self + other

    def __isub__(self, other):
        return self - other

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __rmul__(self, other):
        return self * other
    
    def __truediv__(self, other):
        return self * (1/other)

    def dot(self, other):
        return self.x * other.x + self.y * other.y
    
    def length(self):
        return (self.x**2 + self.y**2)**0.5
    
    def __repr__(self):
        return f"x: {self.x}, y: {self.y}"