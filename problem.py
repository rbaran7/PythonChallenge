#Author: Roman Baran
#Python-Challenge Submission


from itertools import product

rows = input()
columns = input()
matrix = []
maximum_region = 0
checked_position = set()

for x in xrange(rows):
	matrix.append(map(int, raw_input().split()))

	
def neighbors(x, y, rows, columns):
    neighbor = set()
    for dx, dy in product(xrange(-1, 2), xrange(-1, 2)):
        if 0 <= x + dx < rows and 0 <= y + dy < columns and (dx, dy) != (0, 0):
            neighbor.add((x + dx, y + dy))
    return neighbor


def find_connected_region(x, y):
    cell_in_matrix = set([(x, y)])
    current_cell = set([(x, y)])
    while current_cell:
        next_cell = set()
        for x, y in current_cell:
            for i, j in neighbors(x, y, rows, columns):
                if matrix[i][j] and (i, j) not in current_cell and (i, j) not in cell_in_matrix:
                    next_cell.add((i, j))
        cell_in_matrix.update(current_cell)
        current_cell = next_cell
    checked_position.update(cell_in_matrix)
    return len(cell_in_matrix)


for x in xrange(rows):
    for y in xrange(columns):
        if matrix[x][y] and (x, y) not in checked_position:
            maximum_region = max(maximum_region, find_connected_region(x, y))


print maximum_region
