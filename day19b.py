from utilities import *

arr = parse_single_string(False)

patterns = set(arr[0].split(", "))
designs = arr[2:]
pattern_lengths = np.sort(np.unique([len(p) for p in patterns]))


def count_num_ways(d):
    num_ways = [1]  # num_ways[i] is number of ways to make first i colors of design
    while len(num_ways) < len(d) + 1:
        pos = len(num_ways) - 1
        new_num = 0
        for i in pattern_lengths:
            if i <= len(num_ways) and d[pos - i + 1: pos + 1] in patterns:
                new_num += num_ways[-i]
        num_ways.append(new_num)
    return num_ways[-1]


ans = 0
for d in designs:
    ans += count_num_ways(d)

print(ans)
