from __future__ import annotations

class Matrix():

    def __init__(self, values: list[list[float]]) -> None:
        self.values = values
        self.rows = len(values)
        self.columns = len(values[0])

    def __getitem__(self, index: int) -> list[float]:
        return self.values[index]

    def __eq__(self, other: object) -> bool:

        if not isinstance(other, Matrix):
            return NotImplemented

        if self.rows != other.rows or self.columns != other.columns:
            return False

        for row in range(self.rows): #TODO math.isclose implementation
            for column in range(self.columns):
                if self.values[row][column] != other.values[row][column]:
                    return False
        return True

    def __mul__(self, other: Matrix) -> Matrix:
        if self.columns != other.rows:
            raise ValueError("Matrices cannot be multiplied")

        result = [
            [0.0 for _ in range(other.columns)]
            for _ in range(self.rows)
        ]

        for row in range(self.rows):
            for column in range(other.columns):
                for k in range(self.columns):
                    result[row][column] += (
                        self[row][k] * other[k][column]
                    )

        return Matrix(result)