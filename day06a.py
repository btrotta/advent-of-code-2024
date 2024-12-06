from utilities import *

arr = parse_multi_string(False, sep="")
arr_out = []
translate = {".": 0, "#": 1, "^": -1}
for a in arr:
    arr_out.append([translate[ch] for ch in a])
arr = arr_out

j = complex(0, 1)

# get starting position and obstacles
obs = set()
for r in range(len(arr)):
    for c in range(len(arr[0])):
        if arr[r][c] == -1:
            pos = c + r*j
        elif arr[r][c] == 1:
            obs.add(c + r*j)

next_dir = {-j: 1, 1: j, j: -1, -1: -j}


def is_in_map(x):
    return x.real >= 0 and x.real < len(arr[0]) and x.imag >= 0 and x.imag < len(arr)


visited = set()
dir = -j
while True:
    visited.add(pos)
    new_pos = pos + dir
    if not is_in_map(new_pos):
        break
    if new_pos in obs:
        dir = next_dir[dir]
        continue
    pos = new_pos

print(len(visited))
