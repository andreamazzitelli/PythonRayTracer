from typing import List, Union
from raytracer.constants import EPSILON
from raytracer.geometry.tuple import Tuple

class Matrix:
    """Represents a mathematical matrix of arbitrary size (typically 4x4)."""

    def __init__(self, data: List[List[float]]) -> None:
        self.data = data
        self.size = len(data)

    def __getitem__(self, index: int) -> List[float]:
        return self.data[index]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Matrix):
            return NotImplemented
        if self.size != other.size:
            return False
        for r in range(self.size):
            for c in range(self.size):
                if abs(self[r][c] - other[r][c]) > EPSILON:
                    return False
        return True

    def __mul__(self, other: Union['Matrix', Tuple]) -> Union['Matrix', Tuple]:
        if isinstance(other, Matrix):
            result = [[0.0] * self.size for _ in range(self.size)]
            for r in range(self.size):
                for c in range(self.size):
                    result[r][c] = (
                        self[r][0] * other[0][c] +
                        self[r][1] * other[1][c] +
                        self[r][2] * other[2][c] +
                        self[r][3] * other[3][c]
                    )
            return Matrix(result)
        
        elif isinstance(other, Tuple):
            return Tuple(
                self[0][0] * other.x + self[0][1] * other.y + self[0][2] * other.z + self[0][3] * other.w,
                self[1][0] * other.x + self[1][1] * other.y + self[1][2] * other.z + self[1][3] * other.w,
                self[2][0] * other.x + self[2][1] * other.y + self[2][2] * other.z + self[2][3] * other.w,
                self[3][0] * other.x + self[3][1] * other.y + self[3][2] * other.z + self[3][3] * other.w
            )
        return NotImplemented

    def transpose(self) -> 'Matrix':
        """Swaps rows and columns."""
        result = [[self[c][r] for c in range(self.size)] for r in range(self.size)]
        return Matrix(result)

    def determinant(self) -> float:
        """Calculates the determinant of the matrix."""
        if self.size == 2:
            return self[0][0] * self[1][1] - self[0][1] * self[1][0]
        det = 0.0
        for c in range(self.size):
            det += self[0][c] * self.cofactor(0, c)
        return det

    def submatrix(self, row: int, col: int) -> 'Matrix':
        """Returns a new matrix with the specified row and column removed."""
        result = []
        for r in range(self.size):
            if r == row:
                continue
            new_row = [self[r][c] for c in range(self.size) if c != col]
            result.append(new_row)
        return Matrix(result)

    def minor(self, row: int, col: int) -> float:
        """Calculates the determinant of a submatrix."""
        return self.submatrix(row, col).determinant()

    def cofactor(self, row: int, col: int) -> float:
        """Calculates the cofactor (minor with applied sign based on position)."""
        minor_val = self.minor(row, col)
        return -minor_val if (row + col) % 2 != 0 else minor_val

    def inverse(self) -> 'Matrix':
        """Calculates and returns the inverted matrix. Raises ZeroDivisionError if not invertible."""
        det = self.determinant()
        if det == 0:
            raise ZeroDivisionError("Matrix is not invertible (determinant is 0)")
        
        result = [[0.0] * self.size for _ in range(self.size)]
        for r in range(self.size):
            for c in range(self.size):
                # Note the transposition here [c][r] instead of [r][c]
                result[c][r] = self.cofactor(r, c) / det
        return Matrix(result)