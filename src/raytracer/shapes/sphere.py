from typing import List
import math
from raytracer.shapes.shape import Shape
from raytracer.geometry.ray import Ray
from raytracer.geometry.point import Point
from raytracer.geometry.vector import Vector
from raytracer.geometry.intersection import Intersection

class Sphere(Shape):
    """Represents a unit sphere resting at the origin (0, 0, 0)."""
    
    def __init__(self) -> None:
        super().__init__()

    def local_intersect(self, local_ray: Ray) -> List[Intersection]:
        """
        Calculates the intersections of a ray with the sphere using the 
        quadratic formula.
        """
        # The vector from the sphere's center (0,0,0) to the ray origin
        sphere_to_ray = local_ray.origin - Point(0, 0, 0)
        
        a = local_ray.direction.dot(local_ray.direction)
        b = 2.0 * local_ray.direction.dot(sphere_to_ray)
        c = sphere_to_ray.dot(sphere_to_ray) - 1.0
        
        discriminant = (b ** 2) - (4 * a * c)
        
        if discriminant < 0:
            return []  # The ray completely missed the sphere
            
        t1 = (-b - math.sqrt(discriminant)) / (2 * a)
        t2 = (-b + math.sqrt(discriminant)) / (2 * a)
        
        # Always return intersections in ascending order
        return [Intersection(t1, self), Intersection(t2, self)]

    def local_normal_at(self, local_point: Point) -> Vector:
        """
        The normal on a unit sphere at the origin is simply the point 
        minus the origin.
        """
        return local_point - Point(0, 0, 0)