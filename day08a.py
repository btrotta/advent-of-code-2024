from utilities import *
from collections import defaultdict

arr = parse_multi_string(False, "")

j = complex(0, 1)

# get locations of antennae
locs = defaultdict(list)
for r in range(len(arr)):
    for c in range(len(arr[0])):
        if (ch := arr[r][c]) != ".":
            locs[ch].append(r * j + c)

antinodes = set()
for ch, ch_locs in locs.items():
    for i in range(len(ch_locs)):
        for k in range(i + 1, len(ch_locs)):
            dist = ch_locs[k] - ch_locs[i]
            poss_antinodes = [ch_locs[i] - dist, ch_locs[k] + dist]
            for x in poss_antinodes:
                if x.real >= 0 and x.real < len(arr[0]) and x.imag >= 0 and x.imag < len(arr):
                    antinodes.add(x)

print(len(antinodes))
