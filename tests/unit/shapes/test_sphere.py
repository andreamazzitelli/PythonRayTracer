import pytest
import math
from raytracer.shapes.sphere import Sphere
from raytracer.geometry.ray import Ray
from raytracer.geometry.point import Point
from raytracer.geometry.vector import Vector
from raytracer.geometry.transform import translation, scaling, rotation_z

def test_ray_intersects_sphere_at_two_points():
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    s = Sphere()
    xs = s.intersect(r)
    assert len(xs) == 2
    assert xs[0].t == 4.0
    assert xs[1].t == 6.0

def test_ray_intersects_sphere_at_tangent():
    r = Ray(Point(0, 1, -5), Vector(0, 0, 1))
    s = Sphere()
    xs = s.intersect(r)
    assert len(xs) == 2
    assert xs[0].t == 5.0
    assert xs[1].t == 5.0

def test_ray_misses_sphere():
    r = Ray(Point(0, 2, -5), Vector(0, 0, 1))
    s = Sphere()
    xs = s.intersect(r)
    assert len(xs) == 0

def test_ray_originates_inside_sphere():
    r = Ray(Point(0, 0, 0), Vector(0, 0, 1))
    s = Sphere()
    xs = s.intersect(r)
    assert len(xs) == 2
    assert xs[0].t == -1.0
    assert xs[1].t == 1.0

def test_intersecting_scaled_sphere_with_ray():
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    s = Sphere()
    s.transform = scaling(2, 2, 2)
    xs = s.intersect(r)
    assert len(xs) == 2
    assert xs[0].t == 3.0
    assert xs[1].t == 7.0

def test_normal_on_sphere_at_x_axis():
    s = Sphere()
    n = s.normal_at(Point(1, 0, 0))
    assert n == Vector(1, 0, 0)

def test_normal_on_translated_sphere():
    s = Sphere()
    s.transform = translation(0, 1, 0)
    n = s.normal_at(Point(0, 1.70711, -0.70711))
    assert n == Vector(0, 0.70711, -0.70711)

def test_normal_on_transformed_sphere():
    s = Sphere()
    m = scaling(1, 0.5, 1) * rotation_z(math.pi / 5)
    s.transform = m
    n = s.normal_at(Point(0, math.sqrt(2)/2, -math.sqrt(2)/2))
    assert n == Vector(0, 0.97014, -0.24254)