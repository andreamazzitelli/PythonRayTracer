from __future__ import annotations

import math


class Tuple:
    def __init__(self, x: float, y: float, z: float, w: float) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Tuple):
            return NotImplemented

        return (
            math.isclose(self.x, other.x)
            and math.isclose(self.y, other.y)
            and math.isclose(self.z, other.z)
            and math.isclose(self.w, other.w)
        )

    def __neg__(self) -> Tuple:
        return Tuple(
            -self.x,
            -self.y,
            -self.z,
            -self.w,
        )

    def __mul__(self, scalar: float) -> Tuple:
        return Tuple(
            self.x * scalar,
            self.y * scalar,
            self.z * scalar,
            self.w * scalar,
        )

    def __rmul__(self, scalar: float) -> Tuple:
        return self * scalar

    def __truediv__(self, scalar: float) -> Tuple:
        return Tuple(
            self.x / scalar,
            self.y / scalar,
            self.z / scalar,
            self.w / scalar,
        )