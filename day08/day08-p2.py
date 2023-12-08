def at_end(list_):
    for x in list_:
        if not x.endswith('Z'):
            return False
    return True

file = open("input.txt", "r")
instr, graph = tuple(file.readline().strip()), dict()
file.readline() # skip new line
for line in file:
    elem, dst = line.replace('(', '').replace(',', '').replace(')', '').split(' = ')
    graph[elem] = tuple(dst.split())
curr, steps = [k for k in list(graph.keys()) if k.endswith('A')], 0
while True:
    for ch in instr:
        steps += 1
        # print(curr, steps)
        curr = [graph[e][0] if ch == 'L' else graph[e][1] for e in curr]
        if at_end(curr): break
    else:
        continue
    break
print(steps)