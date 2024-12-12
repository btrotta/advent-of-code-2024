from utilities import *
from collections import defaultdict

arr = parse_multi_string(False, sep="")


def get_val(r, c):
    if r < 0 or r >= len(arr) or c < 0 or c >= len(arr[0]):
        return None
    return arr[r][c]

# find connected components and label with distinct labels
edges = {(r, c): [] for r in range(len(arr)) for c in range(len(arr[0]))}
for r in range(len(arr)):
    for c in range(len(arr[0])):
        val = arr[r][c]
        neighbours = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for n in neighbours:
            n_val = get_val(*n)
            if n_val is not None and n_val == val:
                edges[r, c].append(n)

comps = connected_components(edges)
for i, comp in enumerate(comps):
    for r, c in comp:
        arr[r][c] = i

# find areas and perimeters
areas = defaultdict(lambda: 0)
perims = defaultdict(lambda: 0)
for r in range(len(arr)):
    for c in range(len(arr[0])):
        val = arr[r][c]
        areas[val] += 1
        neighbours = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for n in neighbours:
            n_val = get_val(*n)
            if n_val is None or n_val != val:
                perims[val] += 1
ans = 0
for a in areas:
    ans += areas[a] * perims[a]

print(ans)
