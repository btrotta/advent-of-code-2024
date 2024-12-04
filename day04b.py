from utilities import *

arr = parse_multi_string(sep="")
arr = np.array(arr)

ans = 0
for r in range(arr.shape[0] - 2):
    for c in range(arr.shape[1] - 2):
        # check the 3 x 3 array with top-left corner at r, c
        corners = [arr[r, c], arr[r + 2, c], arr[r, c + 2], arr[r + 2, c + 2]]
        centre = arr[r + 1, c + 1]
        if centre == "A" and sorted(corners) == list("MMSS") and corners[0] != corners[3]:
            ans += 1

print(ans)
