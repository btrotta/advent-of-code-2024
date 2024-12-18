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
        edges[r, c] = []
        for r1, c1 in [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]:
            if r1 >= 0 and r1 < size and c1 >= 0 and c1 < size and arr[r1, c1] == 0:
                edges[r, c].append((r1, c1))

ans = shortest_path_unweighted(edges, (0, 0), (size - 1, size - 1))
print(ans)
