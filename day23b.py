from utilities import *

arr = parse_multi_string(False, "-")

edges = defaultdict(list)
for a, b in arr:
    edges[a].append(b)
    edges[b].append(a)


cliques = {tuple(sorted(a)) for a in arr}
largest_clique_size = 2
while True:
    new_cliques = set()
    for curr_clique in cliques:
        for a in curr_clique:
            for b in edges[a]:
                if b in curr_clique:
                    continue
                potential_clique = tuple(sorted(curr_clique + (b, )))
                if potential_clique not in new_cliques and all([b in edges[c] for c in curr_clique]):
                    largest_clique_size = len(curr_clique) + 1
                    new_cliques.add(potential_clique)
    if len(new_cliques) == 0:
        break
    cliques = new_cliques

ans = ",".join(list(cliques)[0])
print(ans)
