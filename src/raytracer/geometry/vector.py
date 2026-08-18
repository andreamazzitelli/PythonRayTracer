import math

class Vector:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):

        if not isinstance(other, Vector):
            return NotImplemented

        return (
            math.isclose(self.x, other.x)
            and math.isclose(self.y, other.y)
            and math.isclose(self.z, other.z)
        )

    def __add__(self, other):

        if not isinstance(other, Vector):
            return NotImplemented

        return Vector(
            self.x + other.x, 
            self.y + other.y, 
            self.z + other.z
        )
        

    def __sub__(self, other):
        
        if not isinstance(other, Vector):
            return NotImplemented

        return Vector(
            self.x - other.x, 
            self.y - other.y, 
            self.z - other.z
        )

    def __neg__(self):
        return Vector(
            -self.x, 
            -self.y, 
            -self.z
            )

    def __mul__(self, other):
        if (not isinstance(other, int)) and (not isinstance(other, float)):
            return NotImplemented
        
        return Vector(
            self.x*other, 
            self.y*other, 
            self.z*other
        )
        
    def __rmul__(self, other):
        return self.__mul__(other)
        
    def __truediv__(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented
        
        return Vector(
            self.x/other, 
            self.y/other, 
            self.z/other
        )

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self):
        return self / self.magnitude()

    def dot(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z) 

    def cross(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        return Vector(
                self.y*other.z - self.z*other.y,
              self.z*other.x - self.x*other.z, 
              self.x*other.y - self.y*other.x
            )

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"