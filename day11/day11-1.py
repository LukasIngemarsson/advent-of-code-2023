# expand rows/cols with no galaxies ("#")
file = open("input.txt", "r")
grid = [list(line.strip()) for line in file]
n, m = len(grid), len(grid[0])
col_expansions, row_expansions = [], []
for i in range(m):
    col = [row[i] for row in grid]
    if all(c == '.' for c in col):
        col_expansions.append(i)
for i, row in enumerate(grid):
    if all(c == '.' for c in row):
        row_expansions.append(i)
for i, col_index in enumerate(col_expansions):
    for j in range(n):
        grid[j].insert(col_index + i, '.')
m = len(grid[0]) # update width
for i, row_index in enumerate(row_expansions):
    grid.insert(row_index + i, ['.'] * m)
n = len(grid) # update height

# assign a unique number to each galaxy from left-right from top-bottom
galaxy_num, galaxies = 1, dict()
for i in range(n):
    for j in range(m):
        if grid[i][j] == '#':
            grid[i][j] = galaxy_num
            galaxies[galaxy_num] = (i, j)
            galaxy_num += 1

# find pairs (ignore duplicates, e.g. (1,2) = (2,1))
pairs = sorted(list(set((i, j) for i in range(galaxy_num) for j in range(i + 1, galaxy_num))))

# implement dijkstras for each pair
ans = 0
for start, end in pairs:
    start_crd, end_crd = galaxies[start], galaxies[end]

    