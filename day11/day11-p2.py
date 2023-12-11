def get_shortest_path_sum(graph, start_node, end_nodes):
    visited, queue, sum_ = [start_node], [[start_node]], 0
    while queue:
        path = queue.pop(0)
        curr = path[-1]
        for neighbor in graph[curr]:
            if neighbor not in visited:
                if neighbor in end_nodes:
                    sum_ += len(path)
                    end_nodes.remove(neighbor)
                    if not end_nodes:
                        print(sum_)
                        return sum_
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                visited.append(neighbor)

# expand rows/cols with no galaxies ("#")
file = open("input.txt", "r")
grid = [list(line.strip()) for line in file]
n, m = len(grid), len(grid[0])

galaxies, graph = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == '#'], {}
for i in range(n):
    for j in range(m):
        neighbors = []
        for dir_ in [(1, 0), (0, -1), (0, 1)]:
            crd = i + dir_[0], j + dir_[1]
            if crd[0] >= 0 and crd[0] < n and crd[1] >= 0 and crd[1] < m:
                neighbors.append(crd)
        graph[(i, j)] = neighbors
ans = 0
for i, glx in enumerate(galaxies[:-1]):
    ans += get_shortest_path_sum(graph, glx, galaxies[i+1:])
print(ans)