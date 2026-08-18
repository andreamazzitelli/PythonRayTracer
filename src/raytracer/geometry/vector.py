import math
from raytracer.geometry.tuple import Tuple

class Vector(Tuple):
    """Represents a directional vector in 3D space (w = 0.0)."""
    
    def __init__(self, x: float, y: float, z: float) -> None:
        super().__init__(x, y, z, 0.0)

    def magnitude(self) -> float:
        """Calculates the length of the vector."""
        return math.sqrt(self.x**2 + self.y**2 + self.z**2 + self.w**2)

    def normalize(self) -> 'Vector':
        """Returns a unit vector (magnitude of 1) in the same direction."""
        mag = self.magnitude()
        return Vector(self.x / mag, self.y / mag, self.z / mag)

    def dot(self, other: Tuple) -> float:
        """Calculates the dot product with another tuple/vector."""
        return (
            self.x * other.x +
            self.y * other.y +
            self.z * other.z +
            self.w * other.w
        )

    def cross(self, other: 'Vector') -> 'Vector':
        """Calculates the cross product, returning a new orthogonal Vector."""
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )