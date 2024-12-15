from utilities import *

arr = parse_single_string(False)

j = complex(0, 1)

dirs = []
boxes = set()
walls = set()
for row, a in enumerate(arr):
    if a.startswith("#"):
        for col, x in enumerate(a):
            loc = -j * row + col
            if x == "@":
                start = loc
            elif x == "#":
                walls.add(loc)
            elif x == "O":
                boxes.add(loc)
    elif a == "":
        continue
    else:
        dirs += list(a)


translate_dir = {">": 1, "<": -1, "^": j, "v": -j}
pos = start
for d in dirs:
    # check if there is a blank space to move into
    boxes_to_move = []
    offset = translate_dir[d]
    new_pos = pos + offset
    if new_pos in walls:
        continue
    while new_pos in boxes:
        boxes_to_move.append(new_pos)
        new_pos += offset
    if new_pos in walls:
        continue
    pos += offset
    if boxes_to_move:
        boxes.remove(boxes_to_move[0])
        boxes.add(boxes_to_move[-1] + offset)

ans = 0
for b in boxes:
    ans += -100 * int(b.imag) + int(b.real)
print(ans)
