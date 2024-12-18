from utilities import *

arr = parse_multi_int(False, sep=",")
bytes = arr

size = 71

arr = np.zeros((size, size))
for x, y in bytes[:1024]:
    arr[x, y] = 1

edges = {}
for r in range(size):
    for c in range(size):
        if arr[r, c] == 1:
            continue
        edges[r, c] = set()
        for r1, c1 in [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]:
            if r1 >= 0 and r1 < size and c1 >= 0 and c1 < size and arr[r1, c1] == 0:
                edges[r, c].add((r1, c1))


def get_shortest_path(edges):
    start = (0, 0)
    end = (size - 1, size - 1)
    visited = set()
    to_visit = deque([[start, 0, []]])
    while len(to_visit) > 0:
        curr, dist, path = to_visit.popleft()
        if curr not in visited:
            visited.add(curr)
            for neighbour in edges[curr]:
                if neighbour == end:
                    return path + [neighbour]
                if neighbour not in visited:
                    to_visit.append([neighbour, dist + 1, path + [neighbour]])
    return None


path = get_shortest_path(edges)
i = 1024
while path is not None and i < len(bytes):
    new_blocks = set()
    while i < len(bytes) and tuple(bytes[i]) not in path:
        new_blocks.add(tuple(bytes[i]))
        i += 1
    if i < len(bytes):
        new_blocks.add(tuple(bytes[i]))
    # update the edges
    for b in new_blocks:
        if b in edges:
            edges.pop(b)
    for k, v in edges.items():
        for b in new_blocks:
            if b in v:
                v.remove(b)
    # try again to find a path
    path = get_shortest_path(edges)

b = bytes[i]
print(",".join(str(x) for x in b))
