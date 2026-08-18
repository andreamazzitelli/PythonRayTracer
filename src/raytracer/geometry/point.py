from raytracer.geometry.tuple import Tuple

class Point(Tuple):
    """Represents a point in 3D space (w = 1.0)."""
    
    def __init__(self, x: float, y: float, z: float) -> None:
        super().__init__(x, y, z, 1.0)