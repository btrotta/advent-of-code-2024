from utilities import *

arr = parse_multi_string(False, "")

edges = {}
walls = []
for r in range(len(arr)):
    for c in range(len(arr[0])):
        if arr[r][c] == "S":
            start = (r, c)
        elif arr[r][c] == "E":
            end = (r, c)
        elif arr[r][c] == "#":
            walls.append((r, c))
        edges[r, c] = []
        for [r1, c1] in [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]:
            if r1 >= 0 and r1 < len(arr) and c1 >= 0 and c1 < len(arr[0]) and arr[r1][c1] in ["E", ".", "S"]:
                edges[r, c].append((r1, c1))


shortest_path_no_cheats = shortest_path_unweighted(edges, start, end)


def get_distance_to_wall(start):
    distances = defaultdict(lambda: np.inf)
    visited = set()
    to_visit = deque([[start, 0]])
    while len(to_visit) > 0:
        curr, dist = to_visit.popleft()
        if curr not in visited:
            visited.add(curr)
            r, c = curr
            for [r1, c1] in [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]:
                if r1 >= 0 and r1 < len(arr) and c1 >= 0 and c1 < len(arr[0]):
                    if arr[r1][c1] == "#":
                        distances[r1, c1] = min(distances[r1, c1], dist + 1)
                    elif (r1, c1) not in visited:
                        to_visit.append([(r1, c1), dist + 1])
    return distances


start_to_wall_dist = get_distance_to_wall(start)
wall_to_end_dist = get_distance_to_wall(end)

ans = 0
for r, c in walls:
    new_dist = start_to_wall_dist[r, c] + wall_to_end_dist[r, c]
    if new_dist <= shortest_path_no_cheats - 100:
        ans += 1
print(ans)
