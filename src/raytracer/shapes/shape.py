from abc import ABC, abstractmethod
from typing import List
from raytracer.geometry.matrix import Matrix
from raytracer.geometry.transform import identity
from raytracer.geometry.ray import Ray
from raytracer.geometry.point import Point
from raytracer.geometry.vector import Vector
from raytracer.geometry.intersection import Intersection
# Note: We will implement Material later. 
# from raytracer.rendering.material import Material 

class Shape(ABC):
    """Abstract base class for all 3D geometry."""
    
    def __init__(self) -> None:
        self.transform: Matrix = identity()
        # self.material = Material() 

    def intersect(self, ray: Ray) -> List[Intersection]:
        """
        Transforms the ray into object space, then calls the shape-specific
        local_intersect method.
        """
        local_ray = ray.transform(self.transform.inverse())
        return self.local_intersect(local_ray)

    @abstractmethod
    def local_intersect(self, local_ray: Ray) -> List[Intersection]:
        """Calculates intersections assuming the ray is in object space."""
        pass

    def normal_at(self, world_point: Point) -> Vector:
        """
        Calculates the surface normal at a given point, converting it 
        back and forth from object space to world space.
        """
        local_point = self.transform.inverse() * world_point
        local_normal = self.local_normal_at(local_point)
        
        # Transform the normal to world space using the transposed inverse
        world_normal = self.transform.inverse().transpose() * local_normal
        
        # Hack to ensure the result remains a vector after transformation
        world_normal.w = 0.0 
        
        return world_normal.normalize()

    @abstractmethod
    def local_normal_at(self, local_point: Point) -> Vector:
        """Calculates the normal vector assuming the point is in object space."""
        pass