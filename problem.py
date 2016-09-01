#author: Roman Baran
#Python Challenge submission

from itertools import product

m = input()
n = input()
matrix = [ ]

for x in xrange(m):
	matrix.append(map(int, raw_input().split()))
	
def neighbors(x, y, m, n):
    neighbor = set()
    for dx, dy in product(xrange(-1, 2), xrange(-1, 2)):
        if 0 <= x + dx < m and 0 <= y + dy < n and (dx, dy) != (0, 0):
            neighbor.add((x+dx, y+dy))
    return neighbor

def find_connected(x, y):
    cell = set([(x, y)])
    current = set([(x, y)])
    while current:
        rowz = set()
        for x, y in current:
            for a, b in neighbors(x, y, m, n):
                if matrix[a][b] and (a, b) not in current and (a, b) not in cell:
                    rowz.add((a, b))
        cell.update(current)
        current = rowz
    seen.update(cell)
    return len(cell)

seen = set()
maximum = 0
for x in xrange(m):
    for y in xrange(n):
        if matrix[x][y] and (x, y) not in seen:
            maximum  = max(maximum, find_connected(x, y))

print maximum

