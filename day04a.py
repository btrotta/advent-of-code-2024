from utilities import *

arr = parse_multi_string(sep="")
arr = np.array(arr)

words = [list("XMAS"), list("SAMX")]
ans = 0
for r in range(arr.shape[0]):
    for c in range(arr.shape[1]):
        if list(arr[r, c:c+4]) in words:
            ans += 1
        if list(arr[r:r+4, c]) in words:
            ans += 1
        if r <= arr.shape[0] - 4 and c <= arr.shape[1] - 4 and [arr[r + i, c + i] for i in range(4)] in words:
            ans += 1
        if r <= arr.shape[0] - 4 and c >= 3 and [arr[r + i, c - i] for i in range(4)] in words:
            ans += 1

print(ans)
