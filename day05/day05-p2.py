file = open("input.txt", "r")
seeds, ranges, expect_new_map = [], [], False
for i, line in enumerate(file):
    if i == 0: # read in seeds
        seeds = [int(x) for x in line.strip().split(':')[1].split()]
    elif line == '\n': # new line, expect new map next iteration
        expect_new_map = True
    elif expect_new_map: # new map
        expect_new_map = False
        new_map = line.strip().replace(' map:', '').split('-to-')
        ranges.append([])
    else: # range
        map_range = [int(x) for x in line.strip().split()] # 0: dest range start, 1: src range start, 2: range length
        ranges[-1].append(map_range)
def find_min_loc():
    seed_ranges = [(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, len(seeds), 2)]
    for loc_val in range(max([r[0] + r[2] for r in ranges[-1]])):
        curr = loc_val
        for range_ in ranges[::-1]:
            for r in range_: 
                if curr >= r[0] and curr < r[0] + r[2]:
                    curr = r[1] + (curr - r[0])
                    break
        for seed_range in seed_ranges:
            if curr >= seed_range[0] and curr <= seed_range[1]:
                return loc_val
print(find_min_loc())