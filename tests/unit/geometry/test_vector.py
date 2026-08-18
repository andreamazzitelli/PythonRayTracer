import math

import pytest

from raytracer.geometry.vector import Vector


def test_vector_creation():
    v = Vector(1, 2, 3)
    assert v.x == 1
    assert v.y == 2
    assert v.z == 3


def test_vector_equality():
    assert Vector(1, 2, 3) == Vector(1, 2, 3)
    assert Vector(1, 2, 3) != Vector(1, 2, 4)


def test_vector_addition():
    assert Vector(1, 2, 3) + Vector(2, 3, 4) == Vector(3, 5, 7)


def test_vector_subtraction():
    assert Vector(1, 2, 3) - Vector(2, 3, 4) == Vector(-1, -1, -1)


def test_vector_scalar_multiplication():
    assert Vector(1, 2, 3) * 3 == Vector(3, 6, 9)


def test_vector_scalar_division():
    assert Vector(2, 4, 6) / 2 == Vector(1, 2, 3)


def test_vector_negation():
    assert -Vector(1, 2, 3) == Vector(-1, -2, -3)


def test_vector_magnitude():
    assert Vector(1, 2, 3).magnitude() == pytest.approx(math.sqrt(14))


def test_vector_normalization():
    assert Vector(4, 0, 0).normalize() == Vector(1, 0, 0)
    assert Vector(1, 2, 3).normalize().magnitude() == pytest.approx(1.0)


def test_vector_dot_product():
    assert Vector(1, 2, 3).dot(Vector(2, 3, 4)) == 20


def test_vector_cross_product():
    a = Vector(1, 2, 3)
    b = Vector(2, 3, 4)

    assert a.cross(b) == Vector(-1, 2, -1)
    assert b.cross(a) == Vector(1, -2, 1)
