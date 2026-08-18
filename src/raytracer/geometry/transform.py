import math
from raytracer.geometry.matrix import Matrix

def identity() -> Matrix:
    """Returns the 4x4 identity matrix."""
    return Matrix([
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ])

def translation(x: float, y: float, z: float) -> Matrix:
    """Returns a matrix representing a translation in 3D space."""
    return Matrix([
        [1.0, 0.0, 0.0, float(x)],
        [0.0, 1.0, 0.0, float(y)],
        [0.0, 0.0, 1.0, float(z)],
        [0.0, 0.0, 0.0, 1.0]
    ])

def scaling(x: float, y: float, z: float) -> Matrix:
    """Returns a matrix representing a scale operation."""
    return Matrix([
        [float(x), 0.0, 0.0, 0.0],
        [0.0, float(y), 0.0, 0.0],
        [0.0, 0.0, float(z), 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ])

def rotation_x(radians: float) -> Matrix:
    """Returns a matrix representing a rotation around the X axis."""
    cos_r = math.cos(radians)
    sin_r = math.sin(radians)
    return Matrix([
        [1.0, 0.0, 0.0, 0.0],
        [0.0, cos_r, -sin_r, 0.0],
        [0.0, sin_r, cos_r, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ])

def rotation_y(radians: float) -> Matrix:
    """Returns a matrix representing a rotation around the Y axis."""
    cos_r = math.cos(radians)
    sin_r = math.sin(radians)
    return Matrix([
        [cos_r, 0.0, sin_r, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [-sin_r, 0.0, cos_r, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ])

def rotation_z(radians: float) -> Matrix:
    """Returns a matrix representing a rotation around the Z axis."""
    cos_r = math.cos(radians)
    sin_r = math.sin(radians)
    return Matrix([
        [cos_r, -sin_r, 0.0, 0.0],
        [sin_r, cos_r, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ])