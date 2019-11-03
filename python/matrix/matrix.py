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
        self.numbers =\
            list(map(lambda n: int(n), re.split("\\s+", matrix_string)))
        print(self.numbers)

    # 9 8 7 | 0 1 2
    # 5 3 2 | 3 4 5
    # 6 6 7 | 6 7 8

    # 1 -> [9, 8, 7]
    # 3 -> [5, 3, 2]
    def row(self, index) -> List[int]:
        row = [x for i, x in enumerate(self.numbers) if i // self.columns == (index-1)]
        return row

    # 9 8 7 | 9 5 6
    # 5 3 2 | 8 3 6
    # 6 6 7 | 7 2 7

    # 1 -> 9 5 6
    # 3 -> 7 2 7
    def column(self, index) -> List[int]:
        column = [x for i, x in enumerate(self.numbers) if i % self.columns == (index-1)]
        return column
