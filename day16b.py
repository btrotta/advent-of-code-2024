from utilities import *
import time
t = time.time()
arr = parse_multi_string(False, "")

j = complex(0, 1)
edges = {}
dirs = [1, j, -1, -j]


def rotations_between_dirs(d1, d2):
    dist = (dirs.index(d2) - dirs.index(d1))
    return min(dist % 4, (-dist) % 4)


for r in range(len(arr)):
    for c in range(len(arr[0])):
        loc = c + r * j
        if arr[r][c] == "S":
            start = (loc, 1)
        elif arr[r][c] == "E":
            end = loc
        for d in dirs:
            edges[loc, d] = {}
            new_loc = loc + d
            edges[loc, d] = {}
            if new_loc.real >= 0 and new_loc.real <= len(arr[0]) and new_loc.imag >= 0 and new_loc.imag <= len(arr) and arr[r][c] != "#":
                edges[loc, d][new_loc, d] = 1
            for new_d in dirs:
                if new_d == d:
                    continue
                edges[loc, d][loc, new_d] = 1000 * rotations_between_dirs(d, new_d)


def shortest_path(edge_dict, from_node, to_node):
    # edge dict should be a dictionary where keys are nodes and values are dictionaries
    # edge_dict[node1][node1] = weight of edge between node 1 and node 2
    # Dijkstra's algorithm using priority queue, modified to find all shortest paths and
    # keep track of paths
    nodes = list(edge_dict.keys())
    tentative_dist = []
    for i, n in enumerate(nodes):
        if n == from_node:
            tentative_dist.append([0, from_node, [from_node]])
        else:
            tentative_dist.append([np.inf, n, []])
    heapq.heapify(tentative_dist)
    dist_map = {n: [np.inf, []] for n in nodes}
    dist_map[from_node] = [0, [[from_node]]]
    while len(tentative_dist) > 0:
        dist, node, path = heapq.heappop(tentative_dist)
        if dist > dist_map[node][0]:
            continue
        for neighbour in edge_dict[node]:
            new_dist = dist_map[node][0] + edge_dict[node][neighbour]
            if new_dist <= dist_map[neighbour][0]:
                new_path = path + [neighbour]
                new_queue_member = [new_dist, neighbour, new_path]
                heapq.heappush(tentative_dist, new_queue_member)
                if new_dist < dist_map[neighbour][0]:
                    dist_map[neighbour][1] = [new_path]
                    dist_map[neighbour][0] = new_dist
                else:
                    dist_map[neighbour][1].append(new_path)
        if node == to_node:
            break
    return dist_map[to_node]

# convert edge dict to use tuple coords since heapify doesn't work with complex numbers
new_edges = {}
for k, d in edges:
    new_edges[(k.real, k.imag), (d.real, d.imag)] = {}
    for k1, d1 in edges[k, d]:
        new_edges[(k.real, k.imag), (d.real, d.imag)][(k1.real, k1.imag), (d1.real, d1.imag)] = edges[k, d][k1, d1]

start = ((start[0].real, start[0].imag), (start[1].real, start[1].imag))
ends = []
for d in dirs:
    ends.append(((end.real, end.imag), (d.real, d.imag)))
shortest = None
shortest_paths = []
for curr_end in ends:
    path_length, paths = shortest_path(new_edges, start, curr_end)
    if shortest is None or path_length < shortest:
        shortest_paths = paths
        shortest = path_length
    elif path_length == shortest:
        shortest_paths += paths
        shortest = path_length
print(shortest)

on_shortest_paths = set()
for i, p in enumerate(shortest_paths):
    for k, node in enumerate(p):
        on_shortest_paths.add(node[0])
print(len(on_shortest_paths))
print(time.time() - t)
