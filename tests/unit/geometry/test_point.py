from raytracer.geometry.point import Point
from raytracer.geometry.vector import Vector


def test_point_creation():
    p = Point(1, 2, 3)
    assert p.x == 1
    assert p.y == 2
    assert p.z == 3


def test_point_plus_vector():
    assert Point(1, 2, 3) + Vector(2, 3, 4) == Point(3, 5, 7)


def test_point_minus_vector():
    assert Point(1, 2, 3) - Vector(2, 3, 4) == Point(-1, -1, -1)


def test_point_minus_point():
    assert Point(3, 5, 7) - Point(1, 2, 3) == Vector(2, 3, 4)
