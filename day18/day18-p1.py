with open("test.txt", "r") as f:
    lines = [line.strip().split()[:2] for line in f.readlines()]
lagoon = {(0, 0)}
pos = (0, 0)
for line in lines:
    dir_, dis = line[0], int(line[1])
    match dir_:
        case 'U':
            get_pos = lambda off, r=pos[0], c=pos[1]: (r - off, c) 
        case 'D':
            get_pos = lambda off, r=pos[0], c=pos[1]: (r + off, c) 
        case 'L':
            get_pos = lambda off, r=pos[0], c=pos[1]: (r, c - off) 
        case 'R':
            get_pos = lambda off, r=pos[0], c=pos[1]: (r, c + off) 
    for i in range(1, dis + 1):
        lagoon.add(get_pos(i))
    pos = get_pos(dis)
c_range = (min(lagoon, key=lambda x: x[1])[1] + 1, max(lagoon, key=lambda x: x[1])[1])
r_range = (min(lagoon, key=lambda x: x[0])[0] + 1, max(lagoon, key=lambda x: x[0])[0])
ans = len(lagoon)
for i in range(*r_range):
    for j in range(*c_range):
        if (i, j) not in lagoon:
            intersections = 0
            for k in range(j + 1, c_range[1] + 2):
                if (i, k) in lagoon:
                    intersections += 1
            if intersections % 2 != 0: # odd number of intersections => inside polygon
                ans += 1
print(ans)