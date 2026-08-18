from __future__ import annotations

class Color:

    def __init__(self, red: float, green: float, blue: float) -> None:
        self.red = red
        self.green = green
        self.blue = blue

    def __eq__(self, value: Color) -> bool:
        return self.red == value.red and self.green == value.green and self.blue == value.blue

    def __add__(self, other: Color) -> Color:
        return Color(
            self.red + other.red,
            self.green + other.green,
            self.blue + other.blue
        )

    def __sub__(self, other: Color) -> Color:
        return Color(
            self.red - other.red,
            self.green - other.green,
            self.blue - other.blue
        )


    def __mul__(self, other: float | int | Color) -> Color:

        if isinstance(other, (float, int)):
            return Color(
                self.red * other,
                self.green * other,
                self.blue * other
            )

        if isinstance(other, Color):
            return Color(
                    self.red * other.red,
                    self.green * other.green,
                    self.blue * other.blue
                )
        
        return NotImplemented
    
    def __rmul__(self, other):
        return self.__mul__(other)

class Canvas:

    def __init__(self, width: int, height: int, color: Color = Color(0, 0, 0)) -> None:
        self.width = width
        self.height = height
        self.color = color
        self.pixels = [
            [Color(color.red, color.green, color.blue) for _ in range(width)]
            for _ in range(height)
        ]

    def write_pixel(self, x: int, y: int, color: Color) -> None:
        self.pixels[y][x] = color

    def pixel_at(self, x:int, y: int) -> Color:
        return self.pixels[y][x]

    def to_ppm(self) -> str:
        lines = [
            "P3",
            f"{self.width} {self.height}",
            "255"
        ]

        for row in self.pixels:
            values = []

            for pixel in row:
                values.extend([
                    self._to_ppm_value(pixel.red),
                    self._to_ppm_value(pixel.green),
                    self._to_ppm_value(pixel.blue),
                ])
            lines.extend(self._split_ppm_line(values))
        return "\n".join(lines) + "\n"


    @staticmethod
    def _to_ppm_value(value: float) -> int:
        value = max(0.0, min(1.0, value))
        return round(value * 255)


    @staticmethod
    def _split_ppm_line(values: list[int]) -> list[str]:
        lines = []
        current = ""

        for value in values:
            value = str(value)

            if current and len(current) + 1 + len(value) > 70:
                lines.append(current)
                current = value
            elif current:
                current += " " + value
            else:
                current = value

        if current:
            lines.append(current)

        return lines