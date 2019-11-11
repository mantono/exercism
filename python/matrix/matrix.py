import re
from typing import List


class Matrix(object):
    rows: List[List[int]]
    columns: List[List[int]]

    def __init__(self, matrix_string: str):
        self.rows = create_rows(matrix_string)
        self.columns = create_columns(matrix_string)

    def row(self, index) -> List[int]:
        return self.rows[index-1]

    def column(self, index) -> List[int]:
        return self.columns[index-1]


# 9 8 7 | 0 1 2
# 5 3 2 | 3 4 5
# 6 6 7 | 6 7 8

# 1 -> [9, 8, 7]
# 2 -> [5, 3, 2]
def create_rows(matrix_string: str) -> List[List[int]]:
    matrix: List[List[int]] = []

    for row in matrix_string.splitlines():
        row_list: List[int] = []
        for cell in row.split():
            row_list.append(int(cell))
        matrix.append(row_list)

    return matrix


# 9 8 7 | 9 5 6
# 5 3 2 | 8 3 6
# 6 6 7 | 7 2 7

# 1 -> 9 5 6
# 3 -> 7 2 7
def create_columns(matrix_string: str) -> List[List[int]]:
    rows: List[List[int]] = create_rows(matrix_string)
    matrix: List[List[int]] = []
    for column in zip(*rows):
        matrix.append(list(column))

    return matrix
