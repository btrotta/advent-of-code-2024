from utilities import *

arr = parse_multi_string(False, "")

edges = {}
wall_adj = set()  # non-wall points adjacent to wall
for r in range(len(arr)):
    for c in range(len(arr[0])):
        if arr[r][c] == "S":
            start = (r, c)
        elif arr[r][c] == "E":
            end = (r, c)
        edges[r, c] = []
        for [r1, c1] in [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]:
            if r1 >= 0 and r1 < len(arr) and c1 >= 0 and c1 < len(arr[0]):
                if arr[r1][c1] != "#":
                    edges[r, c].append((r1, c1))
                elif arr[r][c] != "#" and arr[r1][c1] == "#":
                    wall_adj.add((r, c))


shortest_path_no_cheats = shortest_path_unweighted(edges, start, end)


def get_distance_to_wall_adj(start):
    distances = defaultdict(lambda: np.inf)
    distances[start] = 0
    visited = set()
    to_visit = deque([[start, 0]])
    while len(to_visit) > 0:
        curr, dist = to_visit.popleft()
        if curr not in visited:
            visited.add(curr)
            r, c = curr
            for [r1, c1] in [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]:
                if r1 >= 0 and r1 < len(arr) and c1 >= 0 and c1 < len(arr[0]):
                    if (r1, c1) in wall_adj:
                        distances[r1, c1] = min(distances[r1, c1], dist + 1)
                    if arr[r1][c1] != "#" and (r1, c1) not in visited:
                        to_visit.append([(r1, c1), dist + 1])
    return distances


start_to_wall_dist = get_distance_to_wall_adj(start)
wall_to_end_dist = get_distance_to_wall_adj(end)


ans = 0
for n1 in wall_adj:
    for n2 in wall_adj:
        if n1 == n2:
            continue
        (r1, c1), (r2, c2) = n1, n2
        cheat_distance = abs(r2 - r1) + abs(c1 - c2)
        if cheat_distance <= 20:
            new_dist = start_to_wall_dist[n1] + cheat_distance + wall_to_end_dist[n2]
            if new_dist <= shortest_path_no_cheats - 100:
                ans += 1
print(ans)
