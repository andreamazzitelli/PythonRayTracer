import math

import pytest

from raytracer.geometry.point import Point
from raytracer.rendering.camera import Camera


def test_camera_creation():
    camera = Camera(201, 101, math.pi / 2)

    assert camera.width == 201
    assert camera.height == 101
    assert camera.field_of_view == math.pi / 2


def test_camera_pixel_size_for_horizontal_canvas():
    camera = Camera(201, 101, math.pi / 2)

    assert camera.pixel_size == pytest.approx(0.01, abs=1e-4)


def test_camera_pixel_size_for_vertical_canvas():
    camera = Camera(101, 201, math.pi / 2)

    assert camera.pixel_size == pytest.approx(0.01, abs=1e-4)
