from utils import maximum_path_sum

with open('triangle.txt') as triangle_file:
    triangle = tuple(tuple(map(int, line.split()))
                     for line in triangle_file)

assert maximum_path_sum(rows=triangle,
                        successors_count=2) == 7_273
