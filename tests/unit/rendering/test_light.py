from raytracer.geometry.point import Point
from raytracer.rendering.light import PointLight


def test_point_light_creation():
    intensity = (1, 1, 1)
    position = Point(0, 5, 0)

    light = PointLight(position, intensity)

    assert light.position == position
    assert light.intensity == intensity
