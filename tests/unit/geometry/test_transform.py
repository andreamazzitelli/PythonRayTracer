import math
from raytracer.geometry.transform import translation, scaling, rotation_x, identity
from raytracer.geometry.point import Point
from raytracer.geometry.vector import Vector

def test_translation_point():
    transform = translation(5, -3, 2)
    p = Point(-3, 4, 5)
    assert transform * p == Point(2, 1, 7)

def test_translation_vector():
    transform = translation(5, -3, 2)
    v = Vector(-3, 4, 5)
    # Translation should not affect vectors
    assert transform * v == v

def test_scaling_point():
    transform = scaling(2, 3, 4)
    p = Point(-4, 6, 8)
    assert transform * p == Point(-8, 18, 32)

def test_rotation_x():
    p = Point(0, 1, 0)
    half_quarter = rotation_x(math.pi / 4)
    full_quarter = rotation_x(math.pi / 2)
    
    assert half_quarter * p == Point(0, math.sqrt(2)/2, math.sqrt(2)/2)
    assert full_quarter * p == Point(0, 0, 1)

def test_chaining_transformations():
    p = Point(1, 0, 1)
    a = rotation_x(math.pi / 2)
    b = scaling(5, 5, 5)
    c = translation(10, 5, 7)
    
    # Applied in reverse order
    transform = c * b * a
    assert transform * p == Point(15, 0, 7)