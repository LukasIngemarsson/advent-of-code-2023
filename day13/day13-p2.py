file = open("input.txt", "r")
tot_cols, tot_rows = 0, 0
grid = []
for line in file:
    if line == '\n':
        for i in range(len(grid)-1):
            smudge = False
            for j in range(i+1):
                if not i+j+1 < len(grid):
                    tot_rows += i+1
                    break
                elif not grid[i-j] == grid[i+j+1]:
                    for a, b in zip(grid[i-j], grid[i+j+1]):
                        if a != b:
                            if not smudge:
                                smudge = True
                            else:
                                break          
            else:
                tot_rows += i+1
        for i in range(len(grid[0])-1):
            for j in range(i+1):
                if not i+j+1 < len(grid[0]):
                    tot_cols += i+1
                    break
                elif not [r[i-j] for r in grid] == [r[i+j+1] for r in grid]:
                    break
            else:
                tot_cols += i+1
        grid = []
    else:
        grid.append(line.strip())
print(tot_cols + 100 * tot_rows)