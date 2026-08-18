from __future__ import annotations

import math

from raytracer.geometry.tuple import Tuple


class Vector(Tuple):
    def __init__(self, x: float, y: float, z: float) -> None:
        super().__init__(x, y, z, 0.0)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z,
        )

    def __neg__(self) -> Vector:
        return Vector(
            -self.x,
            -self.y,
            -self.z,
        )

    def __mul__(self, scalar: float) -> Vector:
        return Vector(
            self.x * scalar,
            self.y * scalar,
            self.z * scalar,
        )

    def __rmul__(self, scalar: float) -> Vector:
        return self * scalar

    def __truediv__(self, scalar: float) -> Vector:
        return Vector(
            self.x / scalar,
            self.y / scalar,
            self.z / scalar,
        )

    def magnitude(self) -> float:
        return math.sqrt(
            self.x**2 +
            self.y**2 +
            self.z**2
        )

    def normalize(self) -> Vector:
        magnitude = self.magnitude()

        return Vector(
            self.x / magnitude,
            self.y / magnitude,
            self.z / magnitude,
        )

    def dot(self, other: Vector) -> float:
        return (
            self.x * other.x +
            self.y * other.y +
            self.z * other.z
        )

    def cross(self, other: Vector) -> Vector:
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )