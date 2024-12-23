from utilities import *

arr = parse_multi_string(False, "-")

edges = defaultdict(list)
nodes = []
for a, b in arr:
    edges[a].append(b)
    nodes.append(a)
    edges[b].append(a)


sets3 = set()
for a in sorted(nodes):
    if not a.startswith("t"):
        continue
    for b in edges[a]:
        for c in edges[a]:
            if c == b:
                continue
            if b in edges[c]:
                sets3.add(tuple(sorted([a, b, c])))

print(len(sets3))
