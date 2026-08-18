from raytracer.geometry.matrix import Matrix


def test_matrix_creation():
    matrix = Matrix([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 8, 7, 6],
        [5, 4, 3, 2],
    ])

    assert matrix.rows == 4
    assert matrix.columns == 4

    assert matrix[0][0] == 1
    assert matrix[0][3] == 4
    assert matrix[1][2] == 7
    assert matrix[3][0] == 5

def test_matrix_equality():
    a = Matrix([
        [1, 2],
        [3, 4],
    ])

    b = Matrix([
        [1, 2],
        [3, 4],
    ])

    assert a == b

def test_matrix_inequality():
    a = Matrix([
        [1, 2],
        [3, 4],
    ])

    b = Matrix([
        [1, 2],
        [3, 5],
    ])

    assert a != b

def test_matrix_multiplication():
    a = Matrix([
        [1, 2, 3],
        [4, 5, 6],
    ])

    b = Matrix([
        [7, 8],
        [9, 10],
        [11, 12],
    ])

    result = a * b

    assert result == Matrix([
        [58, 64],
        [139, 154],
    ])