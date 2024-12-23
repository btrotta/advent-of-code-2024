import more_itertools

from utilities import *

arr = parse_multi_string(False, "")


locations_numeric = {"7": [0, 0], "8": [0, 1], "9": [0, 2],
                     "4": [1, 0], "5": [1, 1], "6": [1, 2],
                     "1": [2, 0], "2": [2, 1], "3": [2, 2],
                     "0": [3, 1], "A": [3, 2]}
locations_directional = {"^": [0, 1], "A": [0, 2], "<": [1, 0], "v": [1, 1], ">": [1, 2]}


def get_sequences(locations, sort_order):
    sequences = {}
    for a, (x0, y0) in locations.items():
        for b, (x1, y1) in locations.items():
            h_dist = y1 - y0
            v_dist = x1 - x0
            if a == b:
                sequences[a, b] = []
            else:
                seq = []
                if h_dist < 0:
                    seq += ["<" for i in range(abs(h_dist))]
                else:
                    seq += [">" for i in range(abs(h_dist))]
                if v_dist < 0:
                    seq += ["^" for i in range(abs(v_dist))]
                else:
                    seq += ["v" for i in range(abs(v_dist))]
                seq = sorted(seq, key=lambda x: sort_order.index(x))
                sequences[a, b] = seq
    return sequences


sequences_num = get_sequences(locations_numeric, [">", "^", "<", "v"])
sequences_dir = get_sequences(locations_directional, [">", "^", "v", "<"])


def move_arm_dir(pos, input):
    # move robot arm that operates a directional keypad
    # given current pointing position and input, return new position and whether button is pushed
    # return None for gaps
    if input == "A":
        return pos, True
    if pos == "^":
        move = {"^": None, ">": "A", "v": "v", "<": None}
    elif pos == "A":
        move = {"^": None, ">": None, "v": ">", "<": "^"}
    elif pos == ">":
        move = {"^": "A", ">": None, "v": None, "<": "v"}
    elif pos == "v":
        move = {"^": "^", ">": ">", "v": None, "<": "<"}
    elif pos == "<":
        move = {"^": None, ">": "v", "v": None, "<": None}
    return move[input], False


def move_arm_numeric(pos, input):
    # move arm that operates numeric keypad
    # given current pointing position and input, return new position and whether button is pushed
    # return None for gaps
    if input == "A":
        return pos, True
    if input == "^":
        move = {str(x): str(x + 3) for x in range(1, 7)}
        move.update({str(x): None for x in range(7, 10)})
        move.update({"0": "2", "A": "3"})
    elif input == ">":
        move = {str(x): str(x + 1) for x in [1, 4, 7, 2, 5, 8]}
        move.update({str(x): None for x in [3, 6, 9]})
        move.update({"0": "A", "A": None})
    elif input == "v":
        move = {str(x): str(x - 3) for x in range(4, 10)}
        move.update({"1": None, "2": "0", "3": "A", "0": None, "A": None})
    elif input == "<":
        move = {str(x):  str(x - 1) for x in [2, 5, 8, 3, 6, 9]}
        move.update({str(x): None for x in [1, 4, 7]})
        move.update({"0": None, "A": "0"})
    return move[pos], False


cache = {}
num_keypads = 27


def valid_move(start_pos, seq, is_numeric):
    # check if move is valid, i.e. does not pass over gap
    pos = start_pos
    for x in seq:
        if is_numeric:
            pos, _ = move_arm_numeric(pos, x)
        else:
            pos, _ = move_arm_dir(pos, x)
        if pos is None:
            return False
    return True


def get_shortest_sequence(start_pos, next_button, keypad_idx):
    # shortest sequence of button presses on keypad 0 to press next_button
    # on keypad_idx
    # start_pos is positions of arm pointing to keypad_idx
    # assume all previous robot arms point to A, since this must be the case if a button
    # has just been pressed on keypad
    if keypad_idx == 0:
        return 1
    if (start_pos, next_button, keypad_idx) in cache:
        return cache[start_pos, next_button, keypad_idx]
    if start_pos == next_button:
        return 1
    is_numeric = keypad_idx == num_keypads - 1
    if is_numeric:
        moves = sequences_num[start_pos, next_button]
    else:
        moves = sequences_dir[start_pos, next_button]
    shortest = np.inf
    for perm in more_itertools.distinct_permutations(moves):
        if not valid_move(start_pos, perm, is_numeric):
            continue
        curr_shortest = 0
        curr_start_pos = "A"
        perm = "".join(perm) + "A"
        for x in perm:
            curr_shortest += min(shortest, get_shortest_sequence(curr_start_pos, x, keypad_idx - 1))
            curr_start_pos = x
        shortest = min(curr_shortest, shortest)
    cache[start_pos, next_button, keypad_idx] = shortest
    return shortest


ans = 0
for a in arr:
    target_seq = "".join(a)
    start_pos = "A"
    shortest_path = 0
    for x in target_seq:
        shortest_path += get_shortest_sequence(start_pos, x, num_keypads - 1)
        start_pos = x
    numeric_part = int("".join(x for x in a if x.isdigit()))
    ans += numeric_part * shortest_path
print(ans)
