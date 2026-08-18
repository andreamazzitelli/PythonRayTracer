import math
from typing import Union
from raytracer.constants import EPSILON

class Tuple:
    """Base class representing a 4-component tuple used for 3D graphics."""
    
    def __init__(self, x: float, y: float, z: float, w: float) -> None:
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.w = float(w)

    def __add__(self, other: 'Tuple') -> 'Tuple':
        return Tuple(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
            self.w + other.w
        )

    def __sub__(self, other: 'Tuple') -> 'Tuple':
        return Tuple(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z,
            self.w - other.w
        )

    def __neg__(self) -> 'Tuple':
        return Tuple(-self.x, -self.y, -self.z, -self.w)

    def __mul__(self, scalar: Union[float, int]) -> 'Tuple':
        return Tuple(
            self.x * scalar,
            self.y * scalar,
            self.z * scalar,
            self.w * scalar
        )

    def __rmul__(self, scalar: Union[float, int]) -> 'Tuple':
        """Handles scalar * Tuple multiplication (e.g., 3 * Vector)."""
        return self.__mul__(scalar)

    def __truediv__(self, scalar: Union[float, int]) -> 'Tuple':
        return Tuple(
            self.x / scalar,
            self.y / scalar,
            self.z / scalar,
            self.w / scalar
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Tuple):
            return NotImplemented
        return (
            abs(self.x - other.x) < EPSILON and
            abs(self.y - other.y) < EPSILON and
            abs(self.z - other.z) < EPSILON and
            abs(self.w - other.w) < EPSILON
        )

    def is_point(self) -> bool:
        return self.w == 1.0

    def is_vector(self) -> bool:
        return self.w == 0.0