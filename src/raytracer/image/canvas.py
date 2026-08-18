from raytracer.geometry.tuple import Tuple

class Color(Tuple):
    """Represents an RGB color. Treated as a vector (w=0.0) mathematically."""
    def __init__(self, red: float, green: float, blue: float) -> None:
        super().__init__(red, green, blue, 0.0)
        
    @property
    def red(self) -> float: return self.x
    
    @property
    def green(self) -> float: return self.y
    
    @property
    def blue(self) -> float: return self.z

    def __mul__(self, other) -> 'Color':
        # Colors can be multiplied by a scalar or blended with another color (Hadamard product)
        if isinstance(other, Color):
            return Color(self.red * other.red, self.green * other.green, self.blue * other.blue)
        return Color(self.red * other, self.green * other, self.blue * other)


class Canvas:
    """A 2D grid of pixels representing the final image."""
    
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        # Initialize canvas with black pixels
        self.pixels = [[Color(0, 0, 0) for _ in range(width)] for _ in range(height)]

    def write_pixel(self, x: int, y: int, color: Color) -> None:
        """Sets a pixel to a specific color, respecting canvas boundaries."""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.pixels[y][x] = color

    def pixel_at(self, x: int, y: int) -> Color:
        """Retrieves the color at a specific coordinate."""
        return self.pixels[y][x]

    def _clamp(self, value: float) -> int:
        """Clamps a color float (0.0 - 1.0+) into an 8-bit integer (0-255)."""
        scaled = round(value * 255)
        return max(0, min(255, scaled))

    def to_ppm(self) -> str:
        """Generates a plain PPM (P3) string representation of the canvas."""
        header = f"P3\n{self.width} {self.height}\n255\n"
        lines = []
        
        for row in self.pixels:
            current_line = []
            for pixel in row:
                r = self._clamp(pixel.red)
                g = self._clamp(pixel.green)
                b = self._clamp(pixel.blue)
                
                # Ensure lines don't exceed 70 characters as per PPM spec
                for color_val in [str(r), str(g), str(b)]:
                    if len(" ".join(current_line)) + len(color_val) + 1 > 70:
                        lines.append(" ".join(current_line))
                        current_line = [color_val]
                    else:
                        current_line.append(color_val)
            
            if current_line:
                lines.append(" ".join(current_line))
                
        return header + "\n".join(lines) + "\n"