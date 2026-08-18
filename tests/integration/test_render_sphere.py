import pytest

from raytracer.geometry.point import Point
from raytracer.geometry.ray import Ray
from raytracer.geometry.vector import Vector
from raytracer.shapes.sphere import Sphere


def test_rendered_sphere_has_expected_center_hit():
    sphere = Sphere()
    ray = Ray(Point(0, 0, -5), Vector(0, 0, 1))

    intersections = sphere.intersect(ray)

    assert intersections == pytest.approx([4, 6])

    hit = min(t for t in intersections if t >= 0)
    point = ray.position(hit)

    assert point == Point(0, 0, -1)
