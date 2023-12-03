file = open("input.txt", "r")
sum = 0
num_width = 0
engine_grid = [[c for c in line.strip()] + ['.'] for line in file] # append '.' to handle num at end of row
engine_height, engine_width = len(engine_grid), len(engine_grid[0])
for i in range(engine_height):
    for j in range(engine_width):
        if engine_grid[i][j].isdigit():
            num_width += 1
        else:
            if num_width > 0: # search for adjacent symbol
                row_search_bound = (i - 1 if i > 0 else 0,
                                    i + 2 if i + 1 < engine_height else engine_height) 
                col_search_bound = (j - num_width - 1 if j - num_width > 0 else 0, 
                                    j + 1 if j + 1 < engine_width else engine_width)
                for m in range(*row_search_bound):
                    for n in range(*col_search_bound):
                        if not engine_grid[m][n].isdigit() and engine_grid[m][n] != '.':
                            sum += int(''.join(engine_grid[i][j - num_width: j]))
                            break
                    else:
                        continue
                    break
                num_width = 0
print(sum)