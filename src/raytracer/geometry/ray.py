from raytracer.geometry.point import Point
from raytracer.geometry.vector import Vector
from raytracer.geometry.matrix import Matrix

class Ray:
    """Represents a ray of light with a starting origin and a direction."""
    
    def __init__(self, origin: Point, direction: Vector) -> None:
        self.origin = origin
        self.direction = direction

    def position(self, t: float) -> Point:
        """Calculates the position of the ray at distance 't'."""
        # Note: direction is on the left to support our Tuple __rmul__ fix
        return self.origin + self.direction * t

    def transform(self, matrix: Matrix) -> 'Ray':
        """Applies a transformation matrix to the ray's origin and direction."""
        return Ray(
            matrix * self.origin,
            matrix * self.direction
        )