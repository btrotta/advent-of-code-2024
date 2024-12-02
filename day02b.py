from utilities import *

arr = parse_multi_int()

ans = 0
for a in arr:
    for i in range(len(a)):
        new_a = a[:i] + a[i + 1:]
        diffs = np.diff(new_a)
        safe = np.all(np.logical_and(np.abs(diffs) >= 1, np.abs(diffs) <= 3)) and np.min(diffs) * np.max(diffs) > 0
        if safe:
            ans += 1
            break

print(ans)
