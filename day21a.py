from utilities import *

arr = parse_multi_string(False, "")


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


def operate_all(pos, input):
    # pos is positions pointed to by robot 1 (dir), 2 (dir), and 3 (numeric)
    # operate person's keypad, which controls robot 1
    r1_pos, button_push = move_arm_dir(pos[0], input)
    if r1_pos is None:
        return None, False
    if not button_push:
        return (r1_pos, pos[1], pos[2]), False
    # robot 1 presses button it is pointed at and activates robot 2
    r2_pos, button_push = move_arm_dir(pos[1], r1_pos)
    if r2_pos is None:
        return None, False
    if not button_push:
        return (r1_pos, r2_pos, pos[2]), False
    # robot 2 presses button it is pointed at and activates robot 3
    r3_pos, button_push = move_arm_numeric(pos[2], r2_pos)
    if r3_pos is None:
        return None, False
    return (r1_pos, r2_pos, r3_pos), button_push


def get_shortest_path(start_pos, target):
    # return number of minimal-length paths ending in pressing the target button
    # breadth-first search where nodes are tuples of positions of all keypads
    to_visit = deque([[start_pos, 0]])
    shortest_length = np.inf
    visited = set()
    while len(to_visit) > 0:
        pos, dist = to_visit.popleft()
        if pos not in visited:
            visited.add(pos)
            for input in ["^", ">", "v", "<", "A"]:
                new_pos, button_push = operate_all(pos, input)
                if new_pos is not None:
                    if button_push and new_pos[-1] == target:
                        shortest_length = min(shortest_length, dist + 1)
                    if not button_push and dist + 1 < shortest_length:
                        to_visit.append([new_pos, dist + 1])
    return shortest_length


ans = 0
for a in arr:
    pos = ("A", "A", "A")
    shortest_path = 0
    for target in a:
        shortest_path += get_shortest_path(pos, target)
        pos = ("A", "A", target)
    numeric_part = int("".join(x for x in a if x.isdigit()))
    ans += numeric_part * shortest_path
print(ans)

