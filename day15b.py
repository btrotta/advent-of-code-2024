from utilities import *

arr = parse_single_string(False)

j = complex(0, 1)

dirs = []
boxes = set()
walls = set()
for row, a in enumerate(arr):
    if a.startswith("#"):
        for col, x in enumerate(a):
            loc = -j * row + col*2
            if x == "@":
                start = loc
            elif x == "#":
                walls.add(loc)
                walls.add(loc + 1)
            elif x == "O":
                boxes.add(loc)
    elif a == "":
        continue
    else:
        dirs += list(a)


def intersects_box(x):
    # return location of box that intersects x, or None if no such box
    if x in boxes:
        return x
    elif x - 1 in boxes:
        return x - 1
    return None


translate_dir = {">": 1, "<": -1, "^": j, "v": -j}
pos = start
for d in dirs:
    # check if there is a blank space to move into
    boxes_to_move = []
    offset = translate_dir[d]
    new_pos = pos + offset
    if new_pos in walls:
        continue
    if offset in [1, -1]:
        while (b := intersects_box(new_pos)) is not None:
            boxes_to_move.append(b)
            new_pos += offset
        if new_pos in walls:
            continue
    else:
        moving_pos = [pos]
        hit_wall = False
        while moving_pos != [] and not(hit_wall):
            new_moving_pos = []
            for p in moving_pos:
                new_pos = p + offset
                if new_pos in walls:
                    hit_wall = True
                    break
                if (b := intersects_box(new_pos)) is not None:
                    boxes_to_move.append(b)
                    new_moving_pos += [b, b + 1]
            moving_pos = new_moving_pos
        if hit_wall:
            continue
    pos += offset
    if boxes_to_move:
        moved = set()
        for b in boxes_to_move[-1::-1]:
            if b not in moved:
                boxes.remove(b)
                moved.add(b)
                boxes.add(b + offset)


ans = 0
for b in boxes:
    ans += -100 * int(b.imag) + int(b.real)
print(ans)
