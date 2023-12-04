file = open("input.txt", "r")
ans = 0
for line in file:
    card = 0
    line = line.strip().replace('  ', ' ').split(':')[1].split('|')
    winning_nums, scratch_nums = line[0].split(' '), line[1].split(' ')
    winning_nums = [int(x) for x in winning_nums if x != '']
    scratch_nums = [int(x) for x in scratch_nums if x != '']
    for n in scratch_nums:
        if n in winning_nums:
            card = card * 2 if card > 0 else 1
    ans += card
print(ans)