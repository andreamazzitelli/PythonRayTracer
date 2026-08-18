import math
import pytest
from raytracer.geometry.tuple import Tuple
from raytracer.geometry.point import Point
from raytracer.geometry.vector import Vector

def test_tuple_is_point():
    a = Tuple(4.3, -4.2, 3.1, 1.0)
    assert a.x == 4.3
    assert a.y == -4.2
    assert a.z == 3.1
    assert a.w == 1.0
    assert a.is_point() is True
    assert a.is_vector() is False

def test_tuple_is_vector():
    a = Tuple(4.3, -4.2, 3.1, 0.0)
    assert a.x == 4.3
    assert a.y == -4.2
    assert a.z == 3.1
    assert a.w == 0.0
    assert a.is_point() is False
    assert a.is_vector() is True

def test_point_creates_tuple_with_w_1():
    p = Point(4, -4, 3)
    assert p == Tuple(4, -4, 3, 1)

def test_vector_creates_tuple_with_w_0():
    v = Vector(4, -4, 3)
    assert v == Tuple(4, -4, 3, 0)

def test_add_tuples():
    a1 = Tuple(3, -2, 5, 1)
    a2 = Tuple(-2, 3, 1, 0)
    assert a1 + a2 == Tuple(1, 1, 6, 1)

def test_subtract_two_points():
    p1 = Point(3, 2, 1)
    p2 = Point(5, 6, 7)
    assert p1 - p2 == Vector(-2, -4, -6)

def test_subtract_vector_from_point():
    p = Point(3, 2, 1)
    v = Vector(5, 6, 7)
    assert p - v == Point(-2, -4, -6)

def test_subtract_two_vectors():
    v1 = Vector(3, 2, 1)
    v2 = Vector(5, 6, 7)
    assert v1 - v2 == Vector(-2, -4, -6)

def test_negate_tuple():
    a = Tuple(1, -2, 3, -4)
    assert -a == Tuple(-1, 2, -3, 4)

def test_multiply_tuple_by_scalar():
    a = Tuple(1, -2, 3, -4)
    assert a * 3.5 == Tuple(3.5, -7, 10.5, -14)

def test_divide_tuple_by_scalar():
    a = Tuple(1, -2, 3, -4)
    assert a / 2 == Tuple(0.5, -1, 1.5, -2)

def test_magnitude():
    v1 = Vector(1, 0, 0)
    assert math.isclose(v1.magnitude(), 1)
    v2 = Vector(1, 2, 3)
    assert math.isclose(v2.magnitude(), math.sqrt(14))

def test_normalize():
    v = Vector(4, 0, 0)
    assert v.normalize() == Vector(1, 0, 0)
    v2 = Vector(1, 2, 3)
    assert v2.normalize() == Vector(1 / math.sqrt(14), 2 / math.sqrt(14), 3 / math.sqrt(14))

def test_dot_product():
    a = Vector(1, 2, 3)
    b = Vector(2, 3, 4)
    assert a.dot(b) == 20

def test_cross_product():
    a = Vector(1, 2, 3)
    b = Vector(2, 3, 4)
    assert a.cross(b) == Vector(-1, 2, -1)
    assert b.cross(a) == Vector(1, -2, 1)