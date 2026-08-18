from __future__ import annotations
from typing import overload
from raytracer.geometry.vector import Vector
import math

class Point:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other: Point) -> bool:

        if not isinstance(other, Point):
            return NotImplemented

        return (
            math.isclose(self.x, other.x)
            and math.isclose(self.y, other.y)
            and math.isclose(self.z, other.z)
        )

    def __add__(self, other: Vector) -> Point:

        if not isinstance(other, Vector):
            return NotImplemented

        return Point(
            self.x + other.x, 
            self.y + other.y, 
            self.z + other.z
        )

    @overload
    def __sub__(self, other: Vector ) ->  Vector: ...

    @overload
    def __sub__(self, other: Point) -> Vector: ...

    def __sub__(self, other: Vector | Point) -> Point | Vector:


        if isinstance(other, Vector):

            return Point(
                self.x - other.x, 
                self.y - other.y, 
                self.z - other.z
            )
        if isinstance (other, Point):
            return Vector(
                self.x - other.x, 
                self.y - other.y, 
                self.z - other.z
            )

        return NotImplemented

    def __repr__(self) -> str:
        return f"Point({self.x},{self.y},{self.z})"
