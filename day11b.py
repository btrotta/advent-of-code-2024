from utilities import *

arr = parse_multi_int(False)[0]

cache = {(0, 1): 1}


def evaluate(num, num_blinks, cache):
    if (num, num_blinks) in cache:
        return cache[num, num_blinks]
    if num_blinks == 0:
        ans = 1
    else:
        # guaranteed to cycle through numbers whose lengths are powers of 2
        if num == 0:
            ans = evaluate(1, num_blinks - 1, cache)
        else:
            str_num = str(num)
            if len(str_num) % 2 == 0:
                first_half = int(str_num[:len(str_num) // 2])
                second_half = int(str_num[len(str_num) // 2:])
                ans = evaluate(first_half, num_blinks - 1, cache) + evaluate(second_half, num_blinks - 1, cache)
            else:
                ans = evaluate(num * 2024, num_blinks - 1, cache)
    if num < 100:
        cache[num, num_blinks] = ans
    return ans


ans = 0
for a in arr:
    ans += evaluate(a, 75, cache)

print(ans)
