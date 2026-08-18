import math

import pytest

from raytracer.geometry.point import Point
from raytracer.geometry.ray import Ray
from raytracer.geometry.vector import Vector
from raytracer.shapes.sphere import Sphere


def test_sphere_has_origin_and_radius():
    sphere = Sphere()

    assert sphere.center == Point(0, 0, 0)
    assert sphere.radius == 1


def test_ray_misses_sphere():
    sphere = Sphere()
    ray = Ray(Point(0, 2, -5), Vector(0, 0, 1))

    intersections = sphere.intersect(ray)

    assert intersections == []


def test_ray_hits_sphere_at_two_points():
    sphere = Sphere()
    ray = Ray(Point(0, 0, -5), Vector(0, 0, 1))

    intersections = sphere.intersect(ray)

    assert intersections[0].t == pytest.approx(4)
    assert intersections[1].t == pytest.approx(6)

    assert intersections[0].object == sphere
    assert intersections[1].object == sphere

def test_ray_tangent_to_sphere():
    sphere = Sphere()
    ray = Ray(Point(0, 1, -5), Vector(0, 0, 1))

    intersections = sphere.intersect(ray)

    assert intersections[0].t == pytest.approx(5)


def test_ray_originates_inside_sphere():
    sphere = Sphere()
    ray = Ray(Point(0, 0, 0), Vector(0, 0, 1))

    intersections = sphere.intersect(ray)

    assert intersections[0].t == pytest.approx(-1)
    assert intersections[1].t == pytest.approx(1)


def test_sphere_is_behind_ray():
    sphere = Sphere()
    ray = Ray(Point(0, 0, 5), Vector(0, 0, 1))

    intersections = sphere.intersect(ray)

    assert intersections[0].t == pytest.approx(-6)
    assert intersections[1].t == pytest.approx(-4)


def test_point_on_sphere_has_normal():
    sphere = Sphere()

    normal = sphere.normal_at(Point(1, 0, 0))

    assert normal == Vector(1, 0, 0)


def test_normal_at_non_axial_point():
    sphere = Sphere()

    normal = sphere.normal_at(Point(0, math.sqrt(2) / 2, math.sqrt(2) / 2))

    assert normal == Vector(
        0,
        math.sqrt(2) / 2,
        math.sqrt(2) / 2,
    )


def test_normal_is_normalized():
    sphere = Sphere()

    normal = sphere.normal_at(Point(1, 0, 0))

    assert normal.magnitude() == pytest.approx(1.0)

def test_intersection_is_sorted():
    sphere = Sphere(Point(0, 0, 0), 1)
    ray = Ray(
        Point(0, 0, -5),
        Vector(0, 0, 1)
    )

    intersections = sphere.intersect(ray)

    assert len(intersections) == 2
    assert intersections[0].t == pytest.approx(4)
    assert intersections[1].t == pytest.approx(6)