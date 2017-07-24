from typing import (Any,
                    Iterable,
                    Sequence,
                    Tuple)

from utils import minimum_path_sum


def parse_matrix(lines: Iterable[str],
                 sep: str = ',') -> Iterable[Tuple[int, ...]]:
    for line in lines:
        yield tuple(map(int, line.split(sep)))


def matrix_to_triangle(matrix: Sequence[Sequence[int]],
                       *,
                       fill_value: Any) -> Sequence[Sequence[Any]]:
    triangle = [[fill_value
                 for _ in range(elements_count + 1)]
                for elements_count in range(2 * len(matrix) - 1)]
    for row_index, row in enumerate(matrix):
        for column_index, value in enumerate(row):
            triangle[row_index + column_index][row_index] = value
    return triangle


def minimum_matrix_path_sum(matrix: Sequence[Sequence[int]]) -> int:
    triangle = matrix_to_triangle(matrix,
                                  fill_value=float('inf'))
    return minimum_path_sum(rows=triangle,
                            successors_count=2)


example = ((131, 673, 234, 103, 18),
           (201, 96, 342, 965, 150),
           (630, 803, 746, 422, 111),
           (537, 699, 497, 121, 956),
           (805, 732, 524, 37, 331))

with open('matrix.txt') as matrix_file:
    matrix = tuple(parse_matrix(matrix_file))

assert minimum_matrix_path_sum(example) == 2_427
assert minimum_matrix_path_sum(matrix) == 427_337
