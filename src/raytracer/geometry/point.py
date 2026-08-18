from __future__ import annotations

from raytracer.geometry.tuple import Tuple
from raytracer.geometry.vector import Vector


class Point(Tuple):
    def __init__(self, x: float, y: float, z: float) -> None:
        super().__init__(x, y, z, 1.0)

    def __add__(self, other: Vector) -> Point:
        return Point(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
        )

    def __sub__(self, other: Point | Vector) -> Point | Vector:
        if isinstance(other, Point):
            return Vector(
                self.x - other.x,
                self.y - other.y,
                self.z - other.z,
            )

        if isinstance(other, Vector):
            return Point(
                self.x - other.x,
                self.y - other.y,
                self.z - other.z,
            )

        return NotImplemented