from typing import List, Optional, Any

class Intersection:
    """Represents a point where a ray intersects a shape."""
    
    def __init__(self, t: float, obj: Any) -> None:
        self.t = t
        self.obj = obj  # The shape that was intersected

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Intersection):
            return NotImplemented
        return self.t == other.t and self.obj == other.obj

def hit(intersections: List[Intersection]) -> Optional[Intersection]:
    """
    Identifies the 'hit' from a list of intersections. 
    The hit is the intersection with the lowest non-negative 't' value.
    """
    # Filter out intersections behind the ray origin (t < 0)
    valid_intersections = [i for i in intersections if i.t >= 0]
    
    if not valid_intersections:
        return None
        
    # Return the closest intersection
    return min(valid_intersections, key=lambda i: i.t)