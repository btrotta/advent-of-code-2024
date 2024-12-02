from utilities import *

arr = parse_multi_int()

ans = 0
for a in arr:
    diffs = np.diff(a)
    ans += np.all(np.logical_and(np.abs(diffs) >= 1, np.abs(diffs) <= 3)) and np.min(diffs) * np.max(diffs) > 0

print(ans)
