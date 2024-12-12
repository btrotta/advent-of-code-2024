import numpy as np

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

arr = np.array(arr)

# add a border
arr = np.concatenate([np.full(arr[[0], :].shape, -1), arr, np.full(arr[[0], :].shape, -1)], axis=0)
arr = np.concatenate([np.full(arr[:, [0]].shape, -1), arr, np.full(arr[:, [0]].shape, -1)], axis=1)

# find areas and number of sides
areas = defaultdict(lambda: 0)
sides = defaultdict(lambda: 0)
for r in range(len(arr) - 1):
    # consider edge below row r
    v_diff = arr[r + 1, :] - arr[r, :]
    h_diff_r = np.diff(arr[r, :], prepend=0)
    h_diff_r1 = np.diff(arr[r + 1, :], prepend=0)
    for i in range(1, len(v_diff) - 1):
        areas[arr[r, i]] += 1
        if v_diff[i] != 0:
            if h_diff_r[i] != 0 or v_diff[i - 1] == 0:
                sides[arr[r, i]] += 1
            if h_diff_r1[i] != 0 or v_diff[i- 1] == 0:
                sides[arr[r + 1, i]] += 1
for c in range(len(arr[0]) - 1):
    # consider edge to right of col c
    h_diff = arr[:, c + 1] - arr[:, c]
    v_diff_c = np.diff(arr[:, c], prepend=0)
    v_diff_c1 = np.diff(arr[:, c + 1], prepend=0)
    for i in range(1, len(h_diff) - 1):
        if h_diff[i] != 0:
            if v_diff_c[i] != 0 or h_diff[i - 1] == 0:
                sides[arr[i, c]] += 1
            if v_diff_c1[i] != 0 or h_diff[i - 1] == 0:
                sides[arr[i, c + 1]] += 1

ans = 0
for a in areas:
    if a == -1:
        continue
    ans += areas[a] * sides[a]

print(ans)
