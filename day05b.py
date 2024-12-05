from utilities import *
from functools import cmp_to_key

arr = parse_single_string()

order = set()
updates = []
for a in arr:
    if "|" in a:
        order.add(tuple(int(x) for x in a.split("|")))
    elif "," in a:
        updates.append([int(x) for x in a.split(",")])


def compare(a, b):
    if (a, b) in order:
        return -1
    else:
        return 1


ans = 0
for update in updates:
    sorted_update = sorted(update, key=cmp_to_key(compare))
    if sorted_update != update:
        ans += sorted_update[len(sorted_update) // 2]

print(ans)
