import pytest

from raytracer.geometry.point import Point
from raytracer.geometry.vector import Vector
from raytracer.rendering.light import PointLight
from raytracer.rendering.material import Material
from raytracer.rendering.material import lighting


@pytest.fixture
def material():
    return Material()


@pytest.fixture
def light():
    return PointLight(Point(0, 0, -10), (1, 1, 1))


def test_lighting_with_eye_between_light_and_surface(material, light):
    position = Point(0, 0, 0)
    eye = Vector(0, 0, -1)
    normal = Vector(0, 0, -1)

    result = lighting(material, light, position, eye, normal)

    assert result == pytest.approx((1, 1, 1))


def test_lighting_with_eye_offset_45_degrees(material, light):
    position = Point(0, 0, 0)
    eye = Vector(0, 2**0.5 / 2, -2**0.5 / 2)
    normal = Vector(0, 0, -1)

    result = lighting(material, light, position, eye, normal)

    assert result[0] == pytest.approx(1.0, abs=1e-6)


def test_lighting_with_light_offset_45_degrees(material):
    light = PointLight(Point(0, 10, -10), (1, 1, 1))
    position = Point(0, 0, 0)
    eye = Vector(0, 0, -1)
    normal = Vector(0, 0, -1)

    result = lighting(material, light, position, eye, normal)

    assert result[0] == pytest.approx(0.7364, abs=1e-3)


def test_lighting_with_light_behind_surface(material):
    light = PointLight(Point(0, 0, 10), (1, 1, 1))
    position = Point(0, 0, 0)
    eye = Vector(0, 0, -1)
    normal = Vector(0, 0, -1)

    result = lighting(material, light, position, eye, normal)

    assert result[0] == pytest.approx(0.1)
