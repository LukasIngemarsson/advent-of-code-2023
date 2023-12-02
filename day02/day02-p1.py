sum = 0
file = open("input.txt", "r")
line = file.readline()

content = {'red': 12,
           'green': 13,
           'blue': 14
            }

# id = index 1 in parts
while line:
    parts = line.replace(',', '').replace(':', '').replace('\n', '').replace(';', '').split(' ')
    for i in range(2, len(parts), 2):
        # print(parts[i], parts[i + 1])
        if not int(parts[i]) <= content[parts[i + 1]]:
            break
    else:
        sum += int(parts[1])
    line = file.readline()
print(sum)