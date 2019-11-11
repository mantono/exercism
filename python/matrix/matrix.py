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


def create_rows(matrix_string: str) -> List[List[int]]:
    matrix: List[List[int]] = []

    for row in matrix_string.splitlines():
        row_list: List[int] = []
        for cell in row.split():
            row_list.append(int(cell))
        matrix.append(row_list)

    return matrix


def create_columns(matrix_string: str) -> List[List[int]]:
    rows: List[List[int]] = create_rows(matrix_string)
    matrix: List[List[int]] = [list(column) for column in zip(*rows)]
    return matrix
