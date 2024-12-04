from utilities import *

arr = parse_single_string()

ans = 0
enabled = True
for x in arr:
    last_valid_non_num = None  # record state of current multiplication
    prev_num_str = ""
    curr_num_str = ""
    i = 0
    while i < len(x):
        if not enabled:
            while i < len(x) and x[i:i+4] != "do()":
                i += 1
            if i < len(x) and x[i:i+4] == "do()":
                enabled = True
                i += 4
            else:
                i += 1
        elif x[i:i+7] == "don't()":
            enabled = False
            last_valid_non_num = None
            prev_num_str = ""
            curr_num_str = ""
            i += 7
        elif last_valid_non_num is None:
            if x[i: i+4] == "mul(":
                last_valid_non_num = "("
                i += 4
            else:
                i += 1
        elif last_valid_non_num == "(":
            while x[i].isdigit():
                curr_num_str += x[i]
                i += 1
            if i < len(x) and x[i] == ",":
                last_valid_non_num = ","
                prev_num_str = curr_num_str
                curr_num_str = ""
                i += 1
            else:
                curr_num_str = ""
                last_valid_non_num = None
                i += 1
        elif last_valid_non_num == ",":
            while x[i].isdigit():
                curr_num_str += x[i]
                i += 1
            if i < len(x) and x[i] == ")":
                ans += int(prev_num_str) * int(curr_num_str)
                last_valid_non_num = None
                prev_num_str = ""
                curr_num_str = ""
                i += 1
            else:
                prev_num_str = ""
                curr_num_str = ""
                last_valid_non_num = None
                i += 1

print(ans)
