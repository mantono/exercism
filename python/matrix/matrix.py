import re
from typing import List


class Matrix(object):
    numbers: List[int]
    rows: int
    columns: int

    def __init__(self, matrix_string):
        column_data: List[str] = re.split("\n", matrix_string)
        self.rows = len(column_data)
        self.columns = len(re.split("\\s+", column_data[0]))
        self.numbers = list(
            map(lambda n: int(n), re.split("\\s+", matrix_string))
        )

    def row(self, index) -> List[int]:
        return filter()

    def column(self, index) -> List[int]:
        return self.columns
