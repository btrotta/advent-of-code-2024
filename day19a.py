from utilities import *

arr = parse_single_string(False)

patterns = set(arr[0].split(", "))
designs = arr[2:]
pattern_lengths = np.sort(np.unique([len(p) for p in patterns]))[-1::-1]


def can_make_design(d):
    # depth-first search
    to_visit = [0]
    visited = set()
    while to_visit != []:
        curr = to_visit.pop()  # current position in design
        if curr == len(d):
            return True
        visited.add(curr)
        for p in pattern_lengths:
            if p <= len(d) - curr and d[curr:curr + p] in patterns and curr + p not in visited:
                to_visit.append(curr + p)
    return False


ans = 0
for d in designs:
    if can_make_design(d):
        ans += 1

print(ans)
