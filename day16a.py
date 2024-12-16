from utilities import *

arr = parse_multi_string(True, "")

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
shortest = np.inf
for curr_end in ends:
    shortest = min(shortest, shortest_path(new_edges, start, curr_end))
print(shortest)
