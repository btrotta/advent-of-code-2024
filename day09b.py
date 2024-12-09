from utilities import *

a = parse_single_string(False)[0]

# locations spanned by files and free spaces, left limit is included, right limit is excluded
file_locs = []
free_locs = []


def sum_range(a, b):
    # sum of numbers in range(a, b)
    return (a + b - 1) * (b - a) // 2


ans = 0
curr_loc = 0
for i, ch in enumerate(a):
    x = int(ch)
    if i % 2 == 0:
        file_locs.append([curr_loc, curr_loc + x])
        ans += (i // 2) * sum_range(curr_loc, curr_loc + x)
        curr_loc += x
    else:
        if x > 0:
            free_locs.append([curr_loc, curr_loc + x])
            curr_loc += x

while len(file_locs) > 0:
    file_id = len(file_locs) - 1
    file_start, file_end = file_locs.pop()
    file_space = file_end - file_start
    for i, [start, end] in enumerate(free_locs):
        if file_start <= start:
            break
        if file_space <= end - start:
            ans -= file_id * sum_range(file_start, file_end)
            ans += file_id * sum_range(free_locs[i][0], free_locs[i][0] + file_space)
            free_locs[i][0] += file_space
            break

print(ans)

