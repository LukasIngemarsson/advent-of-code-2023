file = open("input.txt", "r")
scratches, card_matches, used = dict(), [], 0
for i, line in enumerate(file):
    line = line.strip().split(':')[1].split('|')
    winning_nums, scratch_nums = line[0].split(), line[1].split()
    matches = [n for n in scratch_nums if n in winning_nums]
    card_matches.append(len(matches) if matches else 0)
    scratches[i] = scratches.get(i, 0) + 1
while not all(value == 0 for value in scratches.values()):
    for key, val in scratches.items():
        if val > 0:
            for i in range(1, card_matches[key] + 1):
                if key + i < len(card_matches):
                    scratches[key + i] = scratches.get(key + i, 0) + val
            used += val
            scratches[key] = 0   
print(used)