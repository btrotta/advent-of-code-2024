from collections import defaultdict, deque
import numpy as np
import heapq
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


def parse_single_int(use_test_file=False):
    # one int per line
    if use_test_file:
        filename = "test_data.txt"
    else:
        filename = "data.txt"
    with open(filename, "r") as f:
        data = f.readlines()
    arr = [int(i) for i in data]
    return arr


def parse_single_string(use_test_file=False):
    # one string per line
    if use_test_file:
        filename = "test_data.txt"
    else:
        filename = "data.txt"
    with open(filename, "r") as f:
        data = f.readlines()
    arr = [a.replace("\n", "") for a in data]
    return arr


def parse_multi_string(use_test_file=False, sep=" "):
    # multiple strings per line
    if use_test_file:
        filename = "test_data.txt"
    else:
        filename = "data.txt"
    with open(filename, "r") as f:
        data = f.readlines()
    if sep == "":
        arr = [list(a.replace("\n", "")) for a in data]
    else:
        arr = [a.replace("\n", "").split(sep) for a in data]
    return arr


def parse_multi_int(use_test_file=False, sep=" "):
    # multiple ints per line
    if use_test_file:
        filename = "test_data.txt"
    else:
        filename = "data.txt"
    with open(filename, "r") as f:
        data = f.readlines()
    if sep == "":
        arr = [[int(i) for i in list(a.replace("\n", ""))] for a in data]
    else:
        arr = [[int(i) for i in a.replace("\n", "").split(sep)] for a in data]
    return arr


def parse_01(use_test_file=False, zero_char=".", one_char="#"):
    arr = parse_multi_string(use_test_file, sep="")
    arr_out = []
    translate = {zero_char: 0, one_char: 1}
    for a in arr:
        arr_out.append([translate[ch] for ch in a])
    return arr_out


def parse_graph(arr, symmetric=False):
    # arr is iterable of 2-element iterables
    edge_dict = defaultdict(lambda: [])
    for a, b in arr:
        edge_dict[a].append(b)
        if symmetric:
            edge_dict[b].append(a)
    return edge_dict


def shortest_path(edge_dict, from_node, to_node):
    # edge dict should be a dictionary where keys are nodes and values are dictionaries
    # edge_dict[node1][node1] = weight of edge between node 1 and node 2
    # Dijkstra's algorithm using priority queue.
    nodes = list(edge_dict.keys())
    tentative_dist = []
    visited = set()
    for i, n in enumerate(nodes):
        if n == from_node:
            tentative_dist.append([0, from_node])
        else:
            tentative_dist.append([np.inf, n])
    heapq.heapify(tentative_dist)
    dist_map = {n: np.inf for n in nodes}
    dist_map[from_node] = 0
    while len(tentative_dist) > 0:
        dist, node = heapq.heappop(tentative_dist)
        if node in visited:
            continue
        for neighbour in edge_dict[node]:
            if neighbour not in visited:
                new_dist = dist_map[node] + edge_dict[node][neighbour]
                if new_dist < dist_map[neighbour]:
                    # Add a new queue member with the shorter distance. We don't need to
                    # delete the old member because it has lower priority than the new one.
                    new_queue_member = [new_dist, neighbour]
                    heapq.heappush(tentative_dist, new_queue_member)
                    dist_map[neighbour] = new_dist
        if node == to_node:
            break
        visited.add(node)
    return dist_map[to_node]


def shortest_path_unweighted(edges, start, end):
    # use breadth-first search
    # edges is a dict mapping each edge to a list of its neighbours
    visited = set()
    to_visit = deque([[start, 0]])
    while len(to_visit) > 0:
        curr, dist = to_visit.popleft()
        if curr not in visited:
            visited.add(curr)
            for neighbour in edges[curr]:
                if neighbour == end:
                    return dist + 1
                if neighbour not in visited:
                    to_visit.append([neighbour, dist + 1])
    return np.inf


def connected_components(edge_dict):
    nodes = list(edge_dict.keys())
    visited = set()
    components = []
    for node in nodes:
        if node in visited:
            continue
        # use depth-first search to find connected component of this node
        curr_component = []
        to_visit = [node]
        while len(to_visit) > 0:
            node = to_visit.pop()
            if node not in visited:
                visited.add(node)
                curr_component.append(node)
            for neighbour in edge_dict[node]:
                if neighbour not in visited:
                    to_visit.append(neighbour)
        components.append(curr_component)
    return components


def binary_search(arr, condition):
    left = 0
    right = len(arr)
    while right - left > 1:
        mid = left + (right - left) // 2
        if condition(arr[mid]):
            right = mid
        else:
            left = mid
    if condition(arr[left]):
        return left
    else:
        return left + 1


def print_coords_complex(coords):
    min_real = min([c.real for c in coords])
    min_imag = min([c.imag for c in coords])
    new_coords = [c - complex(min_real, min_imag) for c in coords]
    max_real = int(max([c.real for c in new_coords]))
    max_imag = int(max([c.imag for c in new_coords]))
    for row in range(max_imag + 1):
        curr_print_row = ""
        for col in range(max_real + 1):
            if complex(col, max_imag - row) in new_coords:
                curr_print_row += "#"
            else:
                curr_print_row += "-"
        print(curr_print_row)


def print_coords(coords):
    min_r = min([c[0] for c in coords])
    min_c = min([c[1] for c in coords])
    new_coords = [(c[0] - min_r, c[1] - min_c) for c in coords]
    max_r = int(max([c[0] for c in new_coords]))
    max_c = int(max([c[1] for c in new_coords]))
    for row in range(max_r + 1):
        curr_print_row = ""
        for col in range(max_c + 1):
            if (row, col) in new_coords:
                curr_print_row += "#"
            else:
                curr_print_row += "-"
        print(curr_print_row)


def show_image(arr):
    arr = np.array(arr)
    plt.imshow(arr, origin="upper")


def valid_coords(r, c, num_rows, num_cols):
    return (r >= 0) and (c >= 0) and (r < num_rows) and (c < num_cols)

def valid_coords_complex(x, num_rows, num_cols):
    r, c = int(x.real), int(x.imag)
    return (r >= 0) and (c >= 0) and (r < num_rows) and (c < num_cols)


ALPHABET = list("abcdefghijklmnopqrstuvwxyz")

DIRECTIONS = [-1, 1, complex(0, 1), complex(0, -1)]

DIRECTIONS_DIAG = [-1, 1, complex(0, 1), complex(0, -1), complex(1, 1), complex(1, -1), complex(-1, 1), complex(-1, -1)]