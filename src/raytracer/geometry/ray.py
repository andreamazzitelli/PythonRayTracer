from raytracer.geometry.point import Point
from raytracer.geometry.vector import Vector

class Ray():

    def __init__(self, origin: Point, direction: Vector) -> None:
        self.origin = origin
        self.direction = direction

    def position(self, distance: float):
        return self.origin + distance*self.direction