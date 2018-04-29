globally_visited = set([])


def bfs(grid, start):
    visited = set([])
    vertices_to_visit = set([])
    area = 0
    vertices_to_visit.add(start)
    globally_visited.add(start)
    while len(vertices_to_visit) > 0:
        v = list(vertices_to_visit)[0]
        vertices_to_visit.remove(v)
        visited.add(v)
        globally_visited.add(v)
        row, col = v
        if grid[row][col] == 0:
            continue

        if grid[row][col] == 1:
            area += 1
        # find all neighbouring vertices
        for row_offset in (-1, 0, 1):
            for col_offset in (-1, 0, 1):
                if row_offset == 0 and col_offset == 0:
                    continue
                new_row, new_col = row + row_offset, col + col_offset
                if 0 <= new_row < n and 0 <= new_col < m and (new_row, new_col) not in visited:
                    vertices_to_visit.add((new_row, new_col))
    return area


def getBiggestRegion(grid):
    max_size = 0
    for row in range(n):
        for col in range(m):
            if grid[row][col] == 0:
                continue
            if (n, m) in globally_visited:
                continue
            region_size = bfs(grid, (row, col))
            if region_size > max_size:
                max_size = region_size
    return max_size


n = int(input().strip())
m = int(input().strip())
grid = []
for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)
print(getBiggestRegion(grid))
