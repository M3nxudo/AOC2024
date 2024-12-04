# AOC - M3nxudo
import re
grid = []


def is_out_of_bounds(_x, _y):
    global grid
    return _x < 0 or _x >= len(grid) or _y < 0 or _y >= len(grid)


def analyze_sequence(start_coord, end_coord, steps=4, _pattern="XMAS"):
    global grid
    if is_out_of_bounds(end_coord[0], end_coord[1]):
        return False
    dx = 1 if end_coord[0] > start_coord[0] else -1 if end_coord[0] < start_coord[0] else 0
    dy = 1 if end_coord[1] > start_coord[1] else -1 if end_coord[1] < start_coord[1] else 0
    sequ = ''
    for step in range(steps):
        i = start_coord[0] + (step * dx)
        j = start_coord[1] + (step * dy)
        sequ += grid[i][j]
    if re.search(_pattern, sequ):
        return True
    else:
        return False


# Fase 1
fp = 'input.txt'
total_result = 0
total_analyzed = 0
with open(fp, 'r') as f:
    for line in f:
        grid.append(list(line.strip()))
for x in range(len(grid)):
    for y in range(len(grid[0])):
        current_cell = [x, y]
        # Check all 8 directions to build sequences
        directions = [
            [x + 3, y],
            [x - 3, y],
            [x, y + 3],
            [x, y - 3],
            [x + 3, y + 3],
            [x - 3, y - 3],
            [x + 3, y - 3],
            [x - 3, y + 3]
        ]
        for end_cell in directions:
            if analyze_sequence(current_cell, end_cell):
                total_result += 1
print(f"XMAS appears {total_result} times")

# Fase 2
total_cross_mas = 0
for x in range(len(grid)):
    for y in range(len(grid[0])):
        current_cell = [x, y]
        # Check diagonals for Cross pattern
        if (analyze_sequence(current_cell, [x + 2, y + 2], steps=3, _pattern="MAS|SAM") and
                analyze_sequence([x, y + 2], [x + 2, y], steps=3, _pattern="MAS|SAM")):
            total_cross_mas += 1
print(f"X-MAS appears {total_cross_mas} times")
