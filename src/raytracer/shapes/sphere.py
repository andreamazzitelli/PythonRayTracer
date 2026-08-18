
from raytracer.geometry.point import Point
from raytracer.geometry.vector import Vector
from raytracer.geometry.ray import Ray
from raytracer.geometry.intersection import Intersection
from raytracer.constants import EPSILON
import math

class Sphere():

    def __init__(self, center: Point = Point(0, 0, 0), radius: float = 1) -> None:
        self.center = center
        self.radius = radius

    def intersect(self, ray: Ray) -> list[Intersection]:

        sphere_to_ray = ray.origin - self.center
        
        a = ray.direction.dot(ray.direction)
        b = 2 * sphere_to_ray.dot(ray.direction)
        c = sphere_to_ray.dot(sphere_to_ray) - self.radius**2

        delta = b**2 - 4*a*c

        if delta < -EPSILON:
            return []
        elif abs(delta) < EPSILON: # delta == 0
            t = -b / (2*a)
            return [Intersection(t, self)]
        
        sqrt_delta = math.sqrt(delta)
        t1 = (-b - sqrt_delta) / (2 * a)
        t2 = (-b + sqrt_delta) / (2 * a)
        return sorted([
            Intersection(t1, self),
            Intersection(t2, self)
        ], key=lambda x: x.t)


    def normal_at(self, point: Point) -> Vector:
        return (point - self.center).normalize()

        


