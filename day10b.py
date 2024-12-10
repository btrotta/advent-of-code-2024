from utilities import *
from collections import defaultdict

arr = parse_multi_int(False, sep="")

edges = defaultdict(list)

heads = []
for r in range(len(arr)):
    for c in range(len(arr[0])):
        if arr[r][c] == 0:
            heads.append((r, c))
        for x, y in [[r - 1, c], [r + 1, c], [r, c + 1], [r, c - 1]]:
            if x >= 0 and x < len(arr) and y >= 0 and y < len(arr[0]):
                if arr[x][y] == arr[r][c] + 1:
                    edges[r, c].append((x, y))

ans = 0
for h in heads:
    to_visit = deque([h])
    while len(to_visit) > 0:
        curr = to_visit.popleft()
        for neighbour in edges[curr]:
            r, c = neighbour
            if arr[r][c] == 9:
                ans += 1
            else:
                to_visit.append(neighbour)

print(ans)
